# -*- coding: utf-8 -*-
import werkzeug
from collections import OrderedDict

from odoo import conf, http, _
from odoo.http import request
from odoo.exceptions import AccessError, MissingError
from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import pager as portal_pager


class ApprovalPortal(portal.CustomerPortal) :
    
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'approval_count' in counters:
            is_group_approval = self._is_group_approval()
            if(is_group_approval):
                values['approval_count'] = request.env['approval.request'].search_count([])
            else:
                values['approval_count'] = request.env['approval.request'].search_count([('request_owner_id.id', '=', request.env.user.id)])
        return values
    
    def _is_group_approval(self):
        is_approval_manager = request.env.user.has_group('approvals.group_approval_user')
        is_approval_admin = request.env.user.has_group('approvals.group_approval_manager')
        if(is_approval_manager or is_approval_admin):
            return True
        return False
    
    @http.route(['/my/approvals', '/my/approvals/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_approvals(self, page=1, date_begin=None, date_end=None, sortby='date', filterby='all'):
        approvalRequest = request.env['approval.request']
        is_group_approval = self._is_group_approval()
        domain = [('request_owner_id.id', '=', request.env.user.id)]
                
        if(is_group_approval):
            domain = []
            
        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]
            
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': []},
            'new': {'label': _('To Submit'), 'domain': [('request_status', '=', 'new')]},
            'approved': {'label': _('Approved'), 'domain': [('request_status', '=', 'approved')]},
            'cancel': {'label': _('Cancel'), 'domain': [('request_status', '=', 'cancel')]},
        }
        domain += searchbar_filters[filterby]['domain']
        
        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc, id desc'},
            'name': {'label': _('Name'), 'order': 'name asc, id asc'},
        }
        order = searchbar_sortings[sortby]['order']

            
        # count for pager
        count = approvalRequest.search_count(domain)
        # make pager
        pager = portal_pager(
            url='/my/approvals',
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=count,
            page=page,
            step=self._items_per_page
        )
        
        # search the approvals to display, according to the pager data        
        approvals = approvalRequest.search(
            domain,
            order=order,
            limit=self._items_per_page,
            offset=pager['offset']
        )
        
        values = {
            'date': date_begin,
            'approvals': approvals,
            'page_name': 'approval',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
            'default_url': '/my/approvals',
        }
        return http.request.render("onnet_approvals.portal_my_approvals", values)
    
    @http.route("/my/approvals/<int:approval_id>", type="http", auth="user", methods=['GET'], website=True)
    def portal_my_approval(self, approval_id):
        try:
            self._document_check_access('approval.request', int(approval_id))
        except (AccessError, MissingError):
            raise werkzeug.exceptions.NotFound
        approval = request.env['approval.request'].browse(approval_id)
        return request.render("onnet_approvals.approval_portal", {'approval': approval})
    
    @http.route("/my/approvals/<int:approval_id>/approval_portal", type="http", auth="user", methods=['GET'])
    def render_approval_backend_view(self, approval_id):
        try:
            approval = self._document_check_access('approval.request', int(approval_id))
        except (AccessError, MissingError):
            raise werkzeug.exceptions.NotFound
        session_info = request.env['ir.http'].session_info()
        user_context = dict(request.env.context) if request.session.uid else {}
        mods = conf.server_wide_modules or []
        lang = user_context.get("lang")
        translation_hash = request.env['ir.http'].get_web_translations_hash(mods, lang)
        cache_hashes = {
            "translations": translation_hash,
        }
        approval_company = approval.company_id
        session_info.update(
            cache_hashes=cache_hashes,
            action_name='onnet_approvals.onnet_approvals_portal_request_view',
            approval_id=approval.id,
            user_companies={
                'current_company': approval_company.id,
                'allowed_companies': {
                    approval_company.id: {
                        'id': approval_company.id,
                        'name': approval_company.name,
                    },
                },
            })

        return request.render(
            'onnet_approvals.approval_portal_embed',
            {'session_info': session_info},
        )

    @http.route("/my/approvals/create", type="http", auth="user", methods=['GET'], website=True)
    def render_approval_create_view(self):
        return request.render('onnet_approvals.approval_portal_new_request')
    
    @http.route("/my/approvals/create_view_form", type="http", auth="user", methods=['GET'])
    def render_approval_create_view_form(self):
        session_info = request.env['ir.http'].session_info()
        user_context = dict(request.env.context) if request.session.uid else {}
        mods = conf.server_wide_modules or []
        lang = user_context.get("lang")
        translation_hash = request.env['ir.http'].get_web_translations_hash(mods, lang)
        cache_hashes = {
            "translations": translation_hash,
        }
        session_info.update(
            cache_hashes=cache_hashes,
            action_name='onnet_approvals.onnet_approvals_portal_request_view',
            approval_id= False,)

        return request.render(
            'onnet_approvals.approval_portal_new_request_form',
            {'session_info': session_info},
        )
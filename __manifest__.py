# -*- coding: utf-8 -*-
{
    'name': "Approvals Portal",
    'summary': "Approvals Portal module",
    'category': 'Human Resources/Approvals',
    'description': """
    This module manages approvals in view portal
    """,
    'author': "Onnet",
    'version': '0.1',
    'depends': ['base', 'approvals'],
    # always loaded
    'data': [
        'views/approval_request_portal_views.xml',
        'views/approval_request_portal_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'onnet_approvals/static/src/scss/approval_portal.scss',
        ],
        'onnet_approvals.webclient': [
            # --------------------web/assets_backend---------------------------
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_backend_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap_backend'),

            ('include', 'web._assets_core'),

            'web/static/src/libs/fontawesome/css/font-awesome.css',
            'web/static/lib/odoo_ui_icons/*',
            'web/static/src/webclient/navbar/navbar.scss',
            'web/static/src/scss/animation.scss',
            'web/static/src/scss/fontawesome_overridden.scss',
            'web/static/src/scss/mimetypes.scss',
            'web/static/src/scss/ui.scss',
            'web/static/src/views/fields/translation_dialog.scss',
            'web/static/src/legacy/scss/ui.scss',

            'web/static/src/polyfills/clipboard.js',

            'web/static/lib/jquery/jquery.js',
            'web/static/lib/popper/popper.js',
            'web/static/lib/bootstrap/js/dist/dom/data.js',
            'web/static/lib/bootstrap/js/dist/dom/event-handler.js',
            'web/static/lib/bootstrap/js/dist/dom/manipulator.js',
            'web/static/lib/bootstrap/js/dist/dom/selector-engine.js',
            'web/static/lib/bootstrap/js/dist/base-component.js',
            'web/static/lib/bootstrap/js/dist/alert.js',
            'web/static/lib/bootstrap/js/dist/button.js',
            'web/static/lib/bootstrap/js/dist/carousel.js',
            'web/static/lib/bootstrap/js/dist/collapse.js',
            'web/static/lib/bootstrap/js/dist/dropdown.js',
            'web/static/lib/bootstrap/js/dist/modal.js',
            'web/static/lib/bootstrap/js/dist/offcanvas.js',
            'web/static/lib/bootstrap/js/dist/tooltip.js',
            'web/static/lib/bootstrap/js/dist/popover.js',
            'web/static/lib/bootstrap/js/dist/scrollspy.js',
            'web/static/lib/bootstrap/js/dist/tab.js',
            'web/static/lib/bootstrap/js/dist/toast.js',
            'web/static/src/legacy/js/libs/bootstrap.js',
            'web/static/src/legacy/js/libs/jquery.js',

            'base/static/src/css/modules.css',

            'web/static/src/core/utils/transitions.scss',
            'web/static/src/model/**/*',
            'web/static/src/search/**/*',
            'web/static/src/webclient/icons.scss', # variables required in list_controller.scss
            'web/static/src/views/**/*',
            'web/static/src/webclient/**/*',
            ('remove', 'web/static/src/webclient/clickbot/clickbot.js'), # lazy loaded
            ('remove', 'web/static/src/views/form/button_box/*.scss'),

            # remove the report code and whitelist only what's needed
            ('remove', 'web/static/src/webclient/actions/reports/**/*'),
            'web/static/src/webclient/actions/reports/*.js',
            'web/static/src/webclient/actions/reports/*.xml',

            'web/static/src/libs/pdfjs.js',

            'web/static/src/scss/ace.scss',
            'web/static/src/scss/base_document_layout.scss',

            'web/static/src/legacy/scss/dropdown.scss',
            'web/static/src/legacy/scss/fields.scss',
            'base/static/src/scss/res_partner.scss',

            # Form style should be computed before
            'web/static/src/views/form/button_box/*.scss',

            'web/static/src/legacy/xml/base.xml',
            # Don't include dark mode files in light mode
            ('remove', 'web/static/src/**/*.dark.scss'),
            
            # ===========================================================
            
            # --------------------bus/assets_backend---------------------------
            'bus/static/src/*.js',
            'bus/static/src/services/**/*.js',
            'bus/static/src/workers/websocket_worker.js',
            'bus/static/src/workers/websocket_worker_utils.js',
            
            # ===========================================================
            
            # --------------------web_tour/assets_backend---------------------------
            'web_tour/static/src/**/*',
            
            # ===========================================================
            
            # --------------------mail/assets_backend---------------------------
            # depends on BS variables, can't be loaded in assets_primary or assets_secondary
            'mail/static/src/scss/variables/derived_variables.scss',
            'mail/static/src/scss/*.scss',
            'mail/static/lib/**/*',
            ('remove', 'mail/static/lib/odoo_sfu/odoo_sfu.js'),
            ('remove', 'mail/static/lib/lame/lame.js'),
            'mail/static/src/js/**/*',
            'mail/static/src/core/common/**/*',
            'mail/static/src/core/web_portal/**/*',
            'mail/static/src/core/web/**/*',
            'mail/static/src/**/common/**/*',
            'mail/static/src/**/web/**/*',
            ('remove', 'mail/static/src/core/web/wysiwyg.js'),
            ('remove', 'mail/static/src/**/*.dark.scss'),
            # discuss (loaded last to fix dependencies)
            ('remove', 'mail/static/src/discuss/**/*'),
            'mail/static/src/discuss/core/common/**/*',
            'mail/static/src/discuss/core/web/**/*',
            'mail/static/src/discuss/**/common/**/*',
            'mail/static/src/discuss/**/web/**/*',
            ('remove', 'mail/static/src/discuss/**/*.dark.scss'),
            'mail/static/src/views/fields/**/*',
            
            # ===========================================================
            
            # --------------------resource/assets_backend---------------------------
            'resource/static/src/**/*',
            
            # ===========================================================
            
            # --------------------hr/assets_backend---------------------------
            'hr/static/src/**/*',
            
            # ===========================================================
            
            # --------------------product/assets_backend---------------------------
            'product/static/src/js/**/*',
            'product/static/src/product_catalog/**/*.js',
            'product/static/src/product_catalog/**/*.xml',
            'product/static/src/product_catalog/**/*.scss',
            
            # ===========================================================
            
            # --------------------approvals/assets_backend---------------------------
            'approvals/static/src/**/*',
            
            # ===========================================================
            
            # --------------------onnet_approvals/assets_backend---------------------------
            'onnet_approvals/static/src/approval_portal/*',
            
            # ===========================================================
            'web/static/src/start.js'
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}


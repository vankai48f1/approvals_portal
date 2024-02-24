/** @odoo-module **/

import { registry } from "@web/core/registry";
import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";


class ApprovalFormController extends FormController {}
ApprovalFormController.template = "onnet_approvals.ApprovalFormController";

const ApprovalFormView = {
    ...formView,
    Controller: ApprovalFormController,
};

registry.category("views").add("approval_portal_form_view", ApprovalFormView);

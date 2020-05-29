import DS from 'ember-data';
import { countries, language_codes } from '../resources';

export default DS.Model.extend({
  // Basic Inforamation
  erp_bai_0_id: DS.attr({
    label: 'resource.fields.erp_bai_0_id',
    hint: 'resource.hints.erp_bai_0_id',
  }),
  erp_bai_1_name: DS.attr({
    label: 'resource.fields.erp_bai_1_name',
    hint: 'resource.hints.erp_bai_1_name',
  }),
  erp_bai_2_service_organisation: DS.belongsTo('provider', {
    label: 'resource.fields.erp_bai_2_service_organisation',
    hint: 'resource.hints.erp_bai_2_service_organisation',
    formAttrs: {
      optionLabelAttr: 'pd_bai_1_name',
    },
  }),
  erp_bai_3_service_providers: DS.hasMany('provider', {
    label: 'resource.fields.erp_bai_3_service_providers',
    hint: 'resource.hints.erp_bai_2_service_organisation',
  }),
  erp_bai_4_webpage: DS.attr({
    label: 'resource.fields.erp_bai_4_webpage',
    hint: 'resource.hints.erp_bai_4_webpage',
  }),
  providers_names: DS.attr({
    label: 'resource.fields.providers_names',
  }),

  // Marketing fields
  erp_mri_1_description: DS.attr({
    label: 'resource.fields.erp_mri_1_description',
    hint: 'resource.hints.erp_mri_1_description',
    type: 'text',
    formComponent: 'text-editor',
    htmlSafe: true
  }),
  erp_mri_2_tagline: DS.attr({
    label: 'resource.fields.erp_mri_2_tagline',
    hint: 'resource.hints.erp_mri_2_tagline',
  }),
  erp_mri_3_logo: DS.attr({
    label: 'resource.fields.erp_mri_3_logo',
    hint: 'resource.hints.erp_mri_3_logo',
  }),
  erp_mri_4_mulitimedia: DS.attr({
    label: 'resource.fields.erp_mri_4_mulitimedia',
    hint: 'resource.hints.erp_mri_4_mulitimedia',
  }),
  erp_mri_5_target_users: DS.hasMany('target-user', {
    label: 'resource.fields.erp_mri_5_target_users',
    hint: 'resource.hints.erp_mri_5_target_users',
  }),
  erp_mri_6_target_customer_tags: DS.attr({
    label: 'resource.fields.erp_mri_6_target_customer_tags',
    hint: 'resource.hints.erp_mri_6_target_customer_tags',
    formComponent: 'agora-chips',
  }),
  erp_mri_7_use_cases: DS.attr({
    label: 'resource.fields.erp_mri_7_use_cases',
    hint: 'resource.hints.erp_mri_7_use_cases',
    type: 'text',
    formComponent: 'text-editor',
    htmlSafe: true
  }),
  erp_mri_5_target_users_verbose: DS.attr({
    label: 'resource.fields.erp_mri_5_target_users'
  }),
  // classification information
  erp_cli_1_scientific_domain: DS.hasMany('domain', {
    label: 'resource.fields.erp_cli_1_scientific_domain',
    hint: 'resource.hints.erp_cli_1_scientific_domain',
  }),
  domain_names: DS.attr({
    label: 'resource.fields.domain_names',
  }),
  // TODO: Filter subdomain's ManyArray results according to domain selections
  erp_cli_2_scientific_subdomain: DS.hasMany('subdomain', {
    label: 'resource.fields.erp_cli_2_scientific_subdomain',
    hint: 'resource.hints.erp_cli_2_scientific_subdomain',
  }),
  subdomain_names: DS.attr({
    label: 'resource.fields.subdomain_names',
  }),
  erp_cli_3_category: DS.hasMany('category', {
    label: 'resource.fields.erp_cli_3_category',
    hint: 'resource.hints.erp_cli_3_category',
  }),
  category_names: DS.attr({
    label: 'resource.fields.category_names',
  }),
  // TODO: Filter subcategory's ManyArray results according to category selections
  erp_cli_4_subcategory: DS.hasMany('subcategory', {
      label: 'resource.fields.erp_cli_4_subcategory',
      hint: 'resource.hints.erp_cli_4_subcategory',
    }),
  subcategory_names: DS.attr({
      label: 'resource.fields.subcategory_names',
    }),
  erp_cli_5_tags: DS.attr({
    label: 'resource.fields.erp_cli_5_tags',
    hint: 'resource.hints.erp_cli_5_tags',
    formComponent: 'agora-chips',
  }),
  // Management Information
  erp_mgi_1_helpdesk_webpage: DS.attr({
    label: 'resource.fields.erp_mgi_1_helpdesk_webpage',
    hint: 'resource.hints.erp_mgi_1_helpdesk_webpage',
  }),
  erp_mgi_2_helpdesk_email: DS.attr({
    label: 'resource.fields.erp_mgi_2_helpdesk_email',
    hint: 'resource.hints.erp_mgi_2_helpdesk_email',
  }),
  erp_mgi_3_user_manual: DS.attr({
    label: 'resource.fields.erp_mgi_3_user_manual',
    hint: 'resource.hints.erp_mgi_3_user_manual',
  }),
  erp_mgi_4_terms_of_use: DS.attr({
    label: 'resource.fields.erp_mgi_4_terms_of_use',
    hint: 'resource.hints.erp_mgi_4_terms_of_use',
  }),
  erp_mgi_5_privacy_policy: DS.attr({
    label: 'resource.fields.erp_mgi_5_privacy_policy',
    hint: 'resource.hints.erp_mgi_5_privacy_policy',
  }),
  erp_mgi_6_sla_specification: DS.attr({
    label: 'resource.fields.erp_mgi_6_sla_specification',
    hint: 'resource.hints.erp_mgi_6_sla_specification',
  }),
  erp_mgi_7_training_information: DS.attr({
    label: 'resource.fields.erp_mgi_7_training_information',
    hint: 'resource.hints.erp_mgi_7_training_information',
  }),
  erp_mgi_8_status_monitoring: DS.attr({
    label: 'resource.fields.erp_mgi_8_status_monitoring',
    hint: 'resource.hints.erp_mgi_8_status_monitoring',
  }),
  erp_mgi_9_maintenance: DS.attr({
    label: 'resource.fields.erp_mgi_9_maintenance',
    hint: 'resource.hints.erp_mgi_9_maintenance',
  }),
  // Geographical and Language availability fields
  erp_gla_1_geographical_availability: DS.attr({
    defaultValue: 'Europe',
    label: 'resource.fields.erp_gla_1_geographical_availability',
    hint: 'resource.hints.erp_gla_1_geographical_availability',
    formComponent: 'agora-chips',
    formAttrs: {
      options: countries,
      exactMatch: true,
    }
  }),
  erp_gla_2_language: DS.attr({
    formComponent: 'agora-chips',
    label: 'resource.fields.erp_gla_2_language',
    hint: 'resource.hints.erp_gla_2_language',
    formAttrs: {
      options: language_codes,
      exactMatch: true,
    },
  }),

  main_contact: DS.belongsTo('contact-information', {
    label: 'resource.fields.main_contact',
    hint: 'resource.hints.main_contact',
  }),
  public_contact: DS.belongsTo('contact-information', {
    label: 'resource.fields.public_contact',
    hint: 'resource.hints.public_contact',
  }),

  resource_admins_ids: DS.attr(),

  __api__: {
    serialize: function(hash) {
      // do not send readonly keys to backend
      delete hash['providers_names'];
      delete hash['resource_admins_ids'];
      delete hash['erp_mri_5_target_users_verbose'];
      delete hash['domain_names'];
      delete hash['subdomain_names'];
      delete hash['category_names'];
      delete hash['subcategory_names'];
      return hash;
    },
  },
});

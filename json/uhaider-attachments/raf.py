from tableauhyperapi import SqlType

data = {
    'vendor_directory': [


        ('CompanyName', SqlType.text()),
        ('Name', SqlType.text()),
        ('VendorAddress', SqlType.text()),
        ('PhoneNumbers', SqlType.text()),
        ('Email', SqlType.text()),
        ('DefaultGLAccount', SqlType.text()),
        ('PaymentType', SqlType.text()),
        ('Send1099', SqlType.text()),
        ('WorkersCompExpires', SqlType.text()),
        ('LiabilityInsExpires', SqlType.text()),
        ('EPACertExpires', SqlType.text()),
        ('AutoInsExpires', SqlType.text()),
        ('StateLicExpires', SqlType.text()),
        ('ContractExpires', SqlType.text()),
        ('Tags', SqlType.text()),
        ('VendorStreet1', SqlType.text()),
        ('VendorStreet2', SqlType.text()),
        ('VendorCity', SqlType.text()),
        ('VendorState', SqlType.text()),
        ('VendorZip', SqlType.text()),
        ('VendorId', SqlType.text()),
        ('VendorTrades', SqlType.text()),
        ('DoNotUseForWorkOrder', SqlType.text()),
        ('Terms', SqlType.text()),
        ('FirstName', SqlType.text()),
        ('LastName', SqlType.text()),
    ],

    'work_order': [

        ('Property', SqlType.text()),
        ('Priority', SqlType.text()),
        ('WorkOrderType', SqlType.text()),
        ('HomeWarrantyExpiration', SqlType.text()),
        ('WorkOrderNumber', SqlType.text()),
        ('JobDescription', SqlType.text()),
        ('Instructions', SqlType.text()),
        ('Status', SqlType.text()),
        ('Vendor', SqlType.text()),
        ('UnitName', SqlType.text()),
        ('PrimaryTenant', SqlType.text()),
        ('CreatedAt', SqlType.text()),
        ('EstimateReqOn', SqlType.text()),
        ('EstimatedOn', SqlType.text()),
        ('EstimateAmount', SqlType.text()),
        ('ScheduledStart', SqlType.text()),
        ('ScheduledEnd', SqlType.text()),
        ('WorkCompletedOn', SqlType.text()),
        ('CompletedOn', SqlType.text()),
        ('Amount', SqlType.text()),
        ('Invoice', SqlType.text()),
        ('Recurring', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('PropertyAddress', SqlType.text()),
        ('PropertyStreet1', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('UnitAddress', SqlType.text()),
        ('UnitStreet', SqlType.text()),
        ('UnitStreet2', SqlType.text()),
        ('UnitCity', SqlType.text()),
        ('UnitState', SqlType.text()),
        ('UnitZip', SqlType.text()),
        ('ServiceRequestNumber', SqlType.text()),
        ('ServiceRequestDescription', SqlType.text()),
        ('vendor_id', SqlType.text()),
        ('UnitId', SqlType.text()),
        ('OccupancyId', SqlType.text()),
        ('PrimaryTenantEmail', SqlType.text()),
        ('PrimaryTenantPhoneNumber', SqlType.text()),
        ('CreatedBy', SqlType.text()),
        ('AssignedUser', SqlType.text()),
        ('LastBilledOn', SqlType.text()),
        ('CanceledOn', SqlType.text()),
        ('WorkOrderId', SqlType.text()),
        ('ServiceRequestId', SqlType.text()),
        ('SubmittedByTenant', SqlType.text()),
        ('RequestingTenant', SqlType.text()),
        ('MaintenanceLimit', SqlType.text()),
        ('StatusNotes', SqlType.text()),
        ('FollowUpOn', SqlType.text()),
        ('VendorTrade', SqlType.text()),
    ],

}

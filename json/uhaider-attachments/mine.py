from tableauhyperapi import SqlType

data = {
    'aged_payables_summary': [

        ("PayeeName", SqlType.text()),
        ("AmountPayable", SqlType.double()),
        ("NotYetDue", SqlType.double()),
        ("0To30", SqlType.double()),
        ("30To60", SqlType.double()),
        ("60To90", SqlType.double()),
        ("90Plus", SqlType.double()),
        ("Property", SqlType.text()),
        ("PropertyName", SqlType.text()),
        ("PropertyId", SqlType.int()),
        ("PropertyAddress", SqlType.text()),
        ("PropertyStreet1", SqlType.text()),
        ("PropertyStreet2", SqlType.text()),
        ("PropertyCity", SqlType.text()),
        ("PropertyState", SqlType.text()),
        ("PropertyZip", SqlType.text()),
        ("UnitId", SqlType.int()),
        ("30Plus", SqlType.double()),
        ("60Plus", SqlType.double()),
        ("InvoicePartyId", SqlType.text()),
        ("InvoicePartyType", SqlType.text()),

    ],

    'aged_receivables_detail': [

        ("PayerName", SqlType.text()),
        ("InvoiceOccurredOn", SqlType.date()),
        ("PostingDate", SqlType.date()),
        ("GlAccountNumber", SqlType.text()),
        ("GlAccountName", SqlType.text()),
        ("TotalAmount", SqlType.double()),
        ("AmountReceivable", SqlType.double()),
        ("0To30", SqlType.double()),
        ("30To60", SqlType.double()),
        ("60To90", SqlType.double()),
        ("90Plus", SqlType.double()),
        ("Property", SqlType.text()),
        ("PropertyName", SqlType.text()),
        ("PropertyId", SqlType.int()),
        ("PropertyAddress", SqlType.text()),
        ("PropertyStreet1", SqlType.text()),
        ("PropertyStreet2", SqlType.text()),
        ("PropertyCity", SqlType.text()),
        ("PropertyState", SqlType.text()),
        ("PropertyZip", SqlType.text()),
        ("GlAccountId", SqlType.int()),
        ("FutureCharges", SqlType.double()),
        ("30Plus", SqlType.double()),
        ("60Plus", SqlType.double()),
        ("OccupancyName", SqlType.text()),
        ("GlAccount", SqlType.text()),
        ("UnitAddress", SqlType.text()),
        ("UnitStreet1", SqlType.text()),
        ("UnitStreet2", SqlType.text()),
        ("UnitCity", SqlType.text()),
        ("UnitState", SqlType.text()),
        ("UnitZip", SqlType.text()),
        ("UnitName", SqlType.text()),
        ("UnitType", SqlType.text()),
        ("UnitTags", SqlType.text()),
        ("TenantStatus", SqlType.text()),
        ("PaymentPlan", SqlType.text()),
        ("occupancy_id", SqlType.int()),
        ("UnitId", SqlType.int()),
    ],

    'bill_detail': [
        ("ReferenceNumber", SqlType.text()),
        ("BillDate", SqlType.date()),
        ("DueDate", SqlType.date()),
        ("Account", SqlType.text()),
        ("Property", SqlType.text()),

        ("Unit", SqlType.text()),
        ("PayeeName", SqlType.text()),
        ("Paid", SqlType.double()),
        ("Unpaid", SqlType.double()),
        ("CheckNumber", SqlType.text()),
        ("PaymentDate", SqlType.date()),

        ("Description", SqlType.text()),
        ("PostingDate", SqlType.date()),
        ("AccountName", SqlType.text()),
        ("AccountNumber", SqlType.text()),
        ("PropertyName", SqlType.text()),

        ("PropertyId", SqlType.int()),
        ("PropertyAddress", SqlType.text()),
        ("PropertyStreet", SqlType.text()),
        ("PropertyStreet2", SqlType.text()),
        ("PropertyCity", SqlType.text()),
        ("PropertyState", SqlType.text()),

        ('PropertyZip', SqlType.text()),
        ('WorkOrder', SqlType.text()),
        ("CashAccount", SqlType.text()),
        ('TxnId', SqlType.int()),
        ('UnitId', SqlType.int()),
        ('Quantity', SqlType.double()),

        ('Rate', SqlType.double()),
        ('WorkOrderAssignee', SqlType.text()),
        ('ApprovalStatus', SqlType.text()),
        ('LastApprover', SqlType.text()),
        ('NextApprovers', SqlType.text()),
        ('DaysPendingApproval', SqlType.text()),

        ('BoardApprovalStatus', SqlType.text()),
        ('TxnCreatedAt', SqlType.date()),
        ('TxnUpdatedAt', SqlType.date()),
        ('CreatedBy', SqlType.text()),
        ("BankAccount", SqlType.text()),
        ("OtherPaymentType", SqlType.text()),

        ("PurchaseOrderNumber", SqlType.text()),
        ("PurchaseOrderId", SqlType.int()),
        ("ProjectId", SqlType.int()),
        ("ServiceRequestId", SqlType.int()),
        ("VendorId", SqlType.int()),

    ],

    'cancelled_processes': [
        ('AttachableFor', SqlType.text()),
        ('Property', SqlType.text()),
        ('WorkflowName', SqlType.text()),
        ('CancelledDate', SqlType.text()),
        ('CancelledBy', SqlType.text()),
        ('CancellationReason', SqlType.text()),
    ],

    'charge_detail': [

        ('ChargeDate', SqlType.date()),
        ('ReceiptInfo', SqlType.text()),
        ('GlAccountNumber', SqlType.text()),
        ('GlAccountName', SqlType.text()),
        ('ChargedTo', SqlType.text()),
        ('ChargeAmount', SqlType.double()),
        ('PaidAmount', SqlType.double()),
        ('Unit', SqlType.text()),
        ('UnitAddress', SqlType.text()),
        ('UnitStreet1', SqlType.text()),
        ('UnitStreet2', SqlType.text()),
        ('UnitCity', SqlType.text()),
        ('UnitState', SqlType.text()),
        ('UnitZip', SqlType.text()),
        ('Property', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.int()),
        ('TxnId', SqlType.int()),
        ('PartyId', SqlType.int()),
        ('Owners', SqlType.text()),
        ('PostingDate', SqlType.date()),
        ('UnitID', SqlType.int()),
        ('ReceivedFromID', SqlType.int()),
        ('GlAccountId', SqlType.int()),
    ],

    'chart_of_accounts': [
        ('GlAccountNumber', SqlType.text()),
        ('GlAccountName', SqlType.text()),
        ('GlAccountType', SqlType.text()),  # confusion
        ('SubAccountof', SqlType.text()),
        ('OffsetAccount', SqlType.text()),
        ('Options', SqlType.text()),  # confusion
        ('Hidden', SqlType.text()),
        ('SubjectToTaxAuthority', SqlType.text()),  # confusion
        ('FundAccount', SqlType.text()),
        ('GlAccountId', SqlType.int()),
        ('SubAccountOfId', SqlType.int()),
        ('OffsetAccountId', SqlType.int()),

    ],

    'check_register_detail': [

        ('BankAccount', SqlType.text()),
        ('PayeeName', SqlType.text()),
        ('CheckNumber', SqlType.text()),
        ('Cleared', SqlType.text()),  # confusion
        ('CheckMemo', SqlType.text()),
        ('OccurredDate', SqlType.date()),
        ('PaymentAmount', SqlType.double()),
        ('PropertyName', SqlType.text()),
        ('GLAccountNumber', SqlType.text()),
        ('GlAccountName', SqlType.text()),
        ('InvoiceAmount', SqlType.double()),
        ('Remarks', SqlType.text()),
        ('Reference', SqlType.text()),
        ('ACHBatchGenDate', SqlType.date()),
        ('PropertyAddress', SqlType.text()),
        ('GLAccountId', SqlType.int()),
        ('PropertyId', SqlType.int()),

    ],

    'completed_processes': [
        ('AttachableFor', SqlType.text()),
        ('Property', SqlType.text()),
        ('WorkflowName', SqlType.text()),
        ('CompletedDate', SqlType.text()),

    ],

    'delinquency': [

        ('Unit', SqlType.text()),
        ('Name', SqlType.text()),
        ('TenantStatus', SqlType.text()),
        ('Tags', SqlType.text()),
        ('PhoneNumbers', SqlType.text()),
        ('MoveIn', SqlType.date()),
        ('MoveOut', SqlType.date()),
        ('Deposit', SqlType.double()),
        ('AmountReceivable', SqlType.double()),
        ('DelinquentSubsidyAmount', SqlType.double()),
        ('0To30', SqlType.double()),
        ('30Plus', SqlType.double()),
        ('LastPayment', SqlType.date()),
        ('PaymentAmount', SqlType.double()),
        ('LateCount', SqlType.int()),
        ('PrimaryTenantEmail', SqlType.text()),
        ('UnitType', SqlType.text()),
        ('Property', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.int()),
        ('PropertyAddress', SqlType.text()),
        ('PropertyStreet1', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('NotYetDue', SqlType.double()),
        ('30To60', SqlType.double()),
        ('60Plus', SqlType.double()),
        ('60To90', SqlType.double()),
        ('90Plus', SqlType.double()),
        ('PrepaymentAmount', SqlType.double()),
        ('NSF', SqlType.int()),
        ('CertifiedFundsOnly', SqlType.text()),  # confusion
        ('Rent', SqlType.double()),
        ('DelinquentRent', SqlType.double()),
        ('DelinquencyNotes', SqlType.text()),
        ('MonthlyCharges', SqlType.text()),
        ('RentDueDay', SqlType.int()),
        ('InCollections', SqlType.text()),
        ('CollectionsAgency', SqlType.text()),
        ('UnitId', SqlType.int()),
        ('OccupancyId', SqlType.int()),
        ('PaymentPlan', SqlType.double()),

    ],

    'deposit_register': [

        ('DepositNumber', SqlType.text()),
        ('ReceiptDate', SqlType.date()),
        ('Payer', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('Type', SqlType.text()),
        ('Reference', SqlType.text()),
        ('Description', SqlType.text()),
        ('DepositAmount', SqlType.double()),
        ('ReceiptAmount', SqlType.double()),
        ('Cleared', SqlType.text()),  # confusion
        ('ReceiptDescription', SqlType.text()),
        ('UnitName', SqlType.text()),
        ('PropertyId', SqlType.int()),
        ('UnitId', SqlType.int()),

    ],

    'general_ledger': [

        ('Property', SqlType.text()),
        ('PostDate', SqlType.date()),
        ('PartyName', SqlType.text()),
        ('Type', SqlType.text()),
        ('Reference', SqlType.text()),
        ('Debit', SqlType.double()),
        ('Credit', SqlType.double()),
        ('Balance', SqlType.double()),
        ('Description', SqlType.text()),
        ('GlAccountName', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.int()),
        ('PropertyAddress', SqlType.text()),
        ('PropertyStreet1', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('Unit', SqlType.text()),
        ('Month', SqlType.text()),
        ('Quarter', SqlType.text()),
        ('Year', SqlType.text()),
        ('BankAccount', SqlType.text()),
        ('TxnCreatedAt', SqlType.date()),
        ('TxnUpdatedAt', SqlType.date()),
        ('CreatedBy', SqlType.text()),
        ('Remarks', SqlType.text()),
        ('DepositDate', SqlType.date()),
        ('DepositNumber', SqlType.text()),
        ('CashAccount', SqlType.text()),
        ('PartyId', SqlType.int()),
        ('TxnId', SqlType.int()),
        ('TxnDetailId', SqlType.int()),
        ('UnitId', SqlType.int()),
        ('GlAccountId', SqlType.int()),

    ],


    'gross_potential_rent_enhanced': [

        ('Unit', SqlType.text()),
        ('BdBa', SqlType.text()),
        ('Tenant', SqlType.text()),
        ('GrossPotentialRent', SqlType.text()),
        ('LossToMarket', SqlType.text()),
        ('MonthlyRent', SqlType.text()),
        ('Concessions', SqlType.text()),
        ('VacancyLoss', SqlType.text()),
        ('ModelLoss', SqlType.text()),
        ('RenovationLoss', SqlType.text()),
        ('OfficeLoss', SqlType.text()),
        ('DelinquencyLoss', SqlType.text()),
        ('NetRentIncome', SqlType.text()),
        ('Period', SqlType.text()),
        ('Property', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('PropertyAddress', SqlType.text()),
        ('PropertyStreet1', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('UnitTags', SqlType.text()),
        ('UnitType', SqlType.text()),
        ('OccupancyId', SqlType.text()),
        ('UnitId', SqlType.text()),
        ('MarketRent', SqlType.text()),

    ],
'guest_cards': [
        ('RentCharges', SqlType.text()),
        ('Name', SqlType.text()),
        ('EmailAddress', SqlType.text()),
        ('PhoneNumber', SqlType.text()),
        ('Received', SqlType.text()),
        ('LastActivityDate', SqlType.text()),
        ('LastActivityType', SqlType.text()),
        ('Status', SqlType.text()),
        ('MoveInPreference', SqlType.text()),
        ('MaxRent', SqlType.text()),
        ('BedBathPreference', SqlType.text()),
        ('PetPreference', SqlType.text()),
        ('MonthlyIncome', SqlType.text()),
        ('CreditScore', SqlType.text()),
        ('LeadType', SqlType.text()),
        ('Source', SqlType.text()),
        ('Property', SqlType.text()),
        ('Unit', SqlType.text()),
        ('AssignedUser', SqlType.text()),
        ('AssignedUserID', SqlType.text()),
        ('GuestCardId', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('UnitId', SqlType.text()),
        ('Notes', SqlType.text()),
        ('TenantId', SqlType.text()),

],

    'homeowner_directory': [
        ('Property', SqlType.text()),
        ('Unit', SqlType.text()),
        ('Homeowner', SqlType.text()),
        ('ElectronicDeliveryConsent', SqlType.text()),
        ('Status', SqlType.text()),
        ('RenterOccupiedUnit', SqlType.text()),
        ('HomeownerType', SqlType.text()),
        ('PhoneNumbers', SqlType.text()),
        ('Emails', SqlType.text()),
        ('LockboxId', SqlType.text()),
        ('OwnershipPercentage', SqlType.text()),
        ('Dues', SqlType.text()),
        ('Tags', SqlType.text()),
        ('HomeownerAddress', SqlType.text()),
        ('HomeownerStreet1', SqlType.text()),
        ('HomeownerStreet2', SqlType.text()),
        ('HomeownerCity', SqlType.text()),
        ('HomeownerState', SqlType.text()),
        ('HomeownerZip', SqlType.text()),
        ('HomeownerCountry', SqlType.text()),
        ('HomeownerBirthdate', SqlType.text()),
        ('UnitAddress', SqlType.text()),
        ('UnitStreet1', SqlType.text()),
        ('UnitStreet2', SqlType.text()),
        ('UnitCity', SqlType.text()),
        ('UnitState', SqlType.text()),
        ('UnitZip', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('PropertyAddress', SqlType.text()),
        ('PropertyStreet1', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('FirstName', SqlType.text()),
        ('LastName', SqlType.text()),
        ('CertifiedFundsOnly', SqlType.text()),
        ('EligibleForDuesIncrease', SqlType.text()),
        ('LastDuesIncrease', SqlType.text()),
        ('NextDuesAdjustment', SqlType.text()),
        ('OnlinePortalActivated', SqlType.text()),
        ('OnlinePaymentsRecurringTotal', SqlType.text()),
        ('OnlinePaymentsRecurringCount', SqlType.text()),
        ('OnlinePortalLogin', SqlType.text()),
        ('SendDuesReminders', SqlType.text()),
        ('UnitTags', SqlType.text()),
        ('UnitType', SqlType.text()),
        ('LateFeeType', SqlType.text()),
        ('LateFeeBaseAmount', SqlType.text()),
        ('LateFeeDailyAmount', SqlType.text()),
        ('DuesGraceDays', SqlType.text()),
        ('DuesGraceDayFixedDay', SqlType.text()),
        ('LateFeeGraceBalance', SqlType.text()),
        ('MaxDailyLateFeesAmount', SqlType.text()),
        ('IgnorePartialPayments', SqlType.text()),
        ('PurchaseDate', SqlType.text()),
        ('SaleDate', SqlType.text()),
        ('InsuranceCompanyName', SqlType.text()),
        ('InsuranceExpiration', SqlType.text()),
        ('InsurancePolicyNumber', SqlType.text()),
        ('LicensePlates', SqlType.text()),
        ('Pets', SqlType.text()),
        ('RenterLeaseStartDate', SqlType.text()),
        ('RenterLeaseEndDate', SqlType.text()),
        ('NsfFee', SqlType.text()),
        ('RequireOnlinePaymentsInFull', SqlType.text()),
        ('SelectedHomeownerId', SqlType.text()),
        ('OccupancyId', SqlType.text()),
        ('UnitId', SqlType.text()),
    ],

    'homeowner_vehicle_info': [

        ('Property', SqlType.text()),
        ('Unit', SqlType.text()),
        ('Homeowner', SqlType.text()),
        ('PhoneNumbers', SqlType.text()),
        ('HomeownerStatus', SqlType.text()),
        ('Make', SqlType.text()),
        ('Model', SqlType.text()),
        ('Color', SqlType.text()),
        ('LicensePlate', SqlType.text()),
        ('Year', SqlType.text()),
        ('PermitNumber', SqlType.text()),
        ('UnitId', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('OccupancyId', SqlType.text()),
        ('HomeownerId', SqlType.text()),
        ('RentableItem', SqlType.text()),
        ('in_progress_workflows', SqlType.text()),
        ('AttachableFor', SqlType.text()),
        ('Property', SqlType.text()),
        ('WorkflowName', SqlType.text()),
        ('CurrentStep', SqlType.text()),
        ('Status', SqlType.text()),
        ('DueDate', SqlType.text()),
        ('AssignedTo', SqlType.text()),
    ],

    'lease_expiration_detail': [

        ('Property', SqlType.text()),
        ('Unit', SqlType.text()),
        ('UnitTags', SqlType.text()),
        ('MoveIn', SqlType.text()),
        ('LeaseExpires', SqlType.text()),
        ('MarketRent', SqlType.text()),
        ('Sqft', SqlType.text()),
        ('TenantName', SqlType.text()),
        ('Deposit', SqlType.text()),
        ('Rent', SqlType.text()),
        ('PhoneNumbers', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('PropertyAddress', SqlType.text()),
        ('PropertyStreet1', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('UnitType', SqlType.text()),
        ('LeaseExpiresMonth', SqlType.text()),
        ('UnitId', SqlType.text()),
        ('OccupancyId', SqlType.text()),
        ('OwnerAgent', SqlType.text()),
        ('RentStatus', SqlType.text()),
        ('LegalRent', SqlType.text()),
        ('Owners', SqlType.text()),
        ('LastRentIncrease', SqlType.text()),
        ('NextRentAdjustment', SqlType.text()),
        ('NextRentIncrease', SqlType.text()),
        ('LeaseSignDate', SqlType.text()),
        ('LastLeaseRenewal', SqlType.text()),
        ('Status', SqlType.text()),
        ('RenewalStartDate', SqlType.text()),
        ('NoticeGivenDate', SqlType.text()),
        ('MoveOut', SqlType.text()),
        ('TenantTags', SqlType.text()),
        ('ComputedMarketRent', SqlType.text()),

    ],

    'payment_plans': [
        ('Property', SqlType.text()),
        ('AccountNumber', SqlType.text()),
        ('AccountName', SqlType.text()),
        ('Name', SqlType.text()),
        ('Tags', SqlType.text()),
        ('OriginalCharge', SqlType.text()),
        ('OriginalChargeDate', SqlType.text()),
        ('TotalOutstandingBalance', SqlType.text()),
        ('Month0', SqlType.text()),
        ('Month1', SqlType.text()),
        ('Month2', SqlType.text()),
        ('Month3', SqlType.text()),
        ('Month4', SqlType.text()),
        ('Month5', SqlType.text()),
        ('Month6', SqlType.text()),
        ('Month7', SqlType.text()),
        ('Month8', SqlType.text()),
        ('Month9', SqlType.text()),
        ('Month10', SqlType.text()),
        ('Month11', SqlType.text()),
        ('TxnId', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('PropertyAddress', SqlType.text()),
        ('PropertyStreet', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('GlAccountId', SqlType.text()),
        ('TenantId', SqlType.text()),
        ('OccupancyId', SqlType.text()),
    ],

    'leasing_agent_performance': [

        ('AssignedUser', SqlType.text()),
        ('GuestCards', SqlType.text()),
        ('Showings', SqlType.text()),
        ('Applications', SqlType.text()),
        ('LeasedUnits', SqlType.text()),
        ('AssignedUserID', SqlType.text()),
    ],

    'owner_directory': [

        ('Name', SqlType.text()),
        ('PhoneNumbers', SqlType.text()),
        ('Email', SqlType.text()),
        ('AlternativePayee', SqlType.text()),
        ('PaymentType', SqlType.text()),
        ('LastPaymentDate', SqlType.text()),
        ('HoldPayments', SqlType.text()),
        ('OwnerPacketReports', SqlType.text()),
        ('SendOwnerPacketsByEmail', SqlType.text()),
        ('PropertiesOwned', SqlType.text()),
        ('Tags', SqlType.text()),
        ('OwnerAddress', SqlType.text()),
        ('LastPacketSent', SqlType.text()),
        ('OwnerStreet1', SqlType.text()),
        ('OwnerStreet2', SqlType.text()),
        ('OwnerCity', SqlType.text()),
        ('OwnerState', SqlType.text()),
        ('OwnerZip', SqlType.text()),
        ('OwnerCountry', SqlType.text()),
        ('OwnerId', SqlType.text()),
        ('PropertiesOwnedIDs', SqlType.text()),
        ('NotesForTheOwner', SqlType.text()),
        ('FirstName', SqlType.text()),
        ('LastName', SqlType.text()),

    ],
    'property_budget': [

        ('GlAccountName', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('Year', SqlType.text()),
        ('Jan', SqlType.text()),
        ('Feb', SqlType.text()),
        ('Mar', SqlType.text()),
        ('Apr', SqlType.text()),
        ('May', SqlType.text()),
        ('Jun', SqlType.text()),
        ('Jul', SqlType.text()),
        ('Aug', SqlType.text()),
        ('Sep', SqlType.text()),
        ('Oct', SqlType.text()),
        ('Nov', SqlType.text()),
        ('Dec', SqlType.text()),
        ('Notes', SqlType.text()),
        ('GlAccountId', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('property_directory', SqlType.text()),
        ('Property', SqlType.text()),
        ('MarketRent', SqlType.text()),
        ('Units', SqlType.text()),
        ('SqFt', SqlType.text()),
        ('ManagementFlatFee', SqlType.text()),
        ('ManagementFeePercent', SqlType.text()),
        ('MinimumFee', SqlType.text()),
        ('Reserve', SqlType.text()),
        ('HomeWarrantyExpiration', SqlType.text()),
        ('InsuranceExpiration', SqlType.text()),
        ('TaxYearEnd', SqlType.text()),
        ('Owners', SqlType.text()),
        ('Description', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('PropertyAddress', SqlType.text()),
        ('PropertyStreet1', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('TaxAuthority', SqlType.text()),
        ('PayerName', SqlType.text()),
        ('Portfolio', SqlType.text()),
        ('PremiumLeadsStatus', SqlType.text()),
        ('PremiumLeadsMonthlyCap', SqlType.text()),
        ('PremiumLeadsActivationDate', SqlType.text()),
        ('OwnerIDs', SqlType.text()),
        ('PropertyGroupId', SqlType.text()),

        ('Visibility', SqlType.text()),
        ('MaintenanceLimit', SqlType.text()),
        ('MaintenanceNotes', SqlType.text()),
        ('SiteManagerName', SqlType.text()),
        ('SiteManagerPhoneNumber', SqlType.text()),
        ('ManagementFeeType', SqlType.text()),
        ('LeaseFeeType', SqlType.text()),
        ('LeaseFlatFee', SqlType.text()),
        ('LeaseFeePercent', SqlType.text()),
        ('OwnerPaymentType', SqlType.text()),
        ('PropertyType', SqlType.text()),
        ('PropertyCreatedOn', SqlType.text()),
        ('PropertyCreatedBy', SqlType.text()),
        ('LateFeeType', SqlType.text()),
        ('LateFeeBaseAmount', SqlType.text()),
        ('LateFeeDailyAmount', SqlType.text()),
        ('LateFeeGracePeriod', SqlType.text()),
        ('LateFeeGracePeriodFixedDay', SqlType.text()),
        ('LateFeeGraceBalance', SqlType.text()),
        ('MaxDailyLateFeesAmount', SqlType.text()),
        ('IgnorePartialPayments', SqlType.text()),
        ('YearBuilt', SqlType.text()),
        ('ContractExpirations', SqlType.text()),
        ('ManagementStartDate', SqlType.text()),
        ('ManagementEndDate', SqlType.text()),
        ('ManagementEndReason', SqlType.text()),
        ('AgentOfRecord', SqlType.text()),
        ('PropertyClass', SqlType.text()),
        ('OnlineMaintenanceRequestInstructions', SqlType.text()),
        ('Amenities', SqlType.text()),

    ],

    'property_group_directory': [

        ('PropertyName', SqlType.text()),
        ('PropertyAddress', SqlType.text()),
        ('Property', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('PropertyStreet1', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('PropertyLegacyStreet1', SqlType.text()),
        ('PropertyGroupName', SqlType.text()),
        ('Portfolio', SqlType.text()),
        ('PropertyGroupId', SqlType.text()),
        ('PortfolioId', SqlType.text()),

    ],

    'prospect_source_tracking': [

        ('Source', SqlType.text()),
        ('GuestCards', SqlType.text()),
        ('Showings', SqlType.text()),
        ('Applications', SqlType.text()),
        ('ApprovedApplications', SqlType.text()),
        ('ConvertedTenants', SqlType.text()),

    ],

    'purchase_order': [

        ('PurchaseOrderNumber', SqlType.text()),
        ('Property', SqlType.text()),
        ('Description', SqlType.text()),
        ('Account', SqlType.text()),
        ('UnitName', SqlType.text()),
        ('VendorName', SqlType.text()),
        ('ApprovalStatus', SqlType.text()),
        ('LastApprover', SqlType.text()),
        ('LastApprovedOn', SqlType.text()),
        ('CreatedAt', SqlType.text()),
        ('RequiredBy', SqlType.text()),
        ('Received', SqlType.text()),
        ('Completed', SqlType.text()),
        ('SumOfBills', SqlType.text()),
        ('Amount', SqlType.text()),
        ('AllBills', SqlType.text()),
        ('BilledAmount', SqlType.text()),
        ('PropertyName', SqlType.text()),
        ('PropertyId', SqlType.text()),
        ('PropertyAddress', SqlType.text()),
        ('PropertyStreet1', SqlType.text()),
        ('PropertyStreet2', SqlType.text()),
        ('PropertyCity', SqlType.text()),
        ('PropertyState', SqlType.text()),
        ('PropertyZip', SqlType.text()),
        ('AccountName', SqlType.text()),
        ('AccountNumber', SqlType.text()),
        ('GlAccountId', SqlType.text()),
        ('ShippedTo', SqlType.text()),
        ('CreatedBy', SqlType.text()),
        ('UpdatedAt', SqlType.text()),
        ('Canceled', SqlType.text()),
        ('unit_id', SqlType.text()),
        ('PurchaseOrderId', SqlType.text()),
        ('Instructions', SqlType.text()),
        ('WorkOrders', SqlType.text()),
        ('RevisionInstructions', SqlType.text()),
        ('RevisionAssignee', SqlType.text()),
        ('RevisionRequester', SqlType.text()),
        ('RevisionRequestedDate', SqlType.text()),
        ('RevisionCompletedDate', SqlType.text()),
    ],
}

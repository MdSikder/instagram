from tableauhyperapi import SqlType

data = {
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

}
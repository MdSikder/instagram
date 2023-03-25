from tableauhyperapi import SqlType

data = {
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

}
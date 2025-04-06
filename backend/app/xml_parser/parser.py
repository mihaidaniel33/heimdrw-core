import pandas as pd
import os
from lxml import etree

NAMESPACES = {'nsSAFT': 'mfp:anaf:dgti:d406:declaratie:v1'}


def parse_tax_tables(xml_content: str) -> pd.DataFrame:

    root = etree.parse(xml_content)

    # Extract the TaxTable entries
    tax_table_entries = root.xpath("//nsSAFT:TaxTable/nsSAFT:TaxTableEntry", namespaces=NAMESPACES)

    # Prepare an empty list to store data for DataFrame
    data = []

    # Loop through each TaxTableEntry and extract relevant fields
    for entry in tax_table_entries:
        tax_type = entry.xpath("nsSAFT:TaxType/text()", namespaces=NAMESPACES)
        description = entry.xpath("nsSAFT:Description/text()", namespaces=NAMESPACES)
        tax_code = entry.xpath("nsSAFT:TaxCodeDetails/nsSAFT:TaxCode/text()", namespaces=NAMESPACES)
        tax_percentage = entry.xpath("nsSAFT:TaxCodeDetails/nsSAFT:TaxPercentage/text()", namespaces=NAMESPACES)
        base_rate = entry.xpath("nsSAFT:TaxCodeDetails/nsSAFT:BaseRate/text()", namespaces=NAMESPACES)
        country = entry.xpath("nsSAFT:TaxCodeDetails/nsSAFT:Country/text()", namespaces=NAMESPACES)

        # Add extracted data to the list
        data.append({
            'TaxType': tax_type[0] if tax_type else None,
            'Description': description[0] if description else None,
            'TaxCode': tax_code[0] if tax_code else None,
            'TaxPercentage': tax_percentage[0] if tax_percentage else None,
            'BaseRate': base_rate[0] if base_rate else None,
            'Country': country[0] if country else None,
        })

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)
    return df


def parse_general_ledger_accounts(xml_content: str) -> pd.DataFrame:
    """
    <nsSAFT:GeneralLedgerAccounts>
			<nsSAFT:Account><nsSAFT:AccountID>1012</nsSAFT:AccountID><nsSAFT:AccountDescription>CAPITAL SUBSCRIS VARSAT</nsSAFT:AccountDescription><nsSAFT:StandardAccountID>1012</nsSAFT:StandardAccountID><nsSAFT:AccountType>Pasiv</nsSAFT:AccountType><nsSAFT:AccountCreationDate>2023-02-28</nsSAFT:AccountCreationDate><nsSAFT:OpeningCreditBalance>200.00</nsSAFT:OpeningCreditBalance><nsSAFT:ClosingCreditBalance>200.00</nsSAFT:ClosingCreditBalance></nsSAFT:Account>
			<nsSAFT:Account><nsSAFT:AccountID>1061</nsSAFT:AccountID><nsSAFT:AccountDescription>REZERVE LEGALE</nsSAFT:AccountDescription><nsSAFT:StandardAccountID>1061</nsSAFT:StandardAccountID><nsSAFT:AccountType>Pasiv</nsSAFT:AccountType><nsSAFT:AccountCreationDate>2023-02-28</nsSAFT:AccountCreationDate><nsSAFT:OpeningCreditBalance>40.00</nsSAFT:OpeningCreditBalance><nsSAFT:ClosingCreditBalance>40.00</nsSAFT:ClosingCreditBalance></nsSAFT:Account>
    </nsSAFT:GeneralLedgerAccounts>
    """
    root = etree.parse(xml_content)

    # Extract the Account entries
    account_entries = root.xpath("//nsSAFT:GeneralLedgerAccounts/nsSAFT:Account", namespaces=NAMESPACES)

    # Prepare an empty list to store data for DataFrame
    data = []

    # Loop through each Account and extract relevant fields
    for entry in account_entries:
        account_id = entry.xpath("nsSAFT:AccountID/text()", namespaces=NAMESPACES)
        description = entry.xpath("nsSAFT:AccountDescription/text()", namespaces=NAMESPACES)
        standard_account_id = entry.xpath("nsSAFT:StandardAccountID/text()", namespaces=NAMESPACES)
        account_type = entry.xpath("nsSAFT:AccountType/text()", namespaces=NAMESPACES)
        creation_date = entry.xpath("nsSAFT:AccountCreationDate/text()", namespaces=NAMESPACES)
        opening_credit = entry.xpath("nsSAFT:OpeningCreditBalance/text()", namespaces=NAMESPACES)
        closing_credit = entry.xpath("nsSAFT:ClosingCreditBalance/text()", namespaces=NAMESPACES)

        # Add extracted data to the list
        data.append({
            'AccountID': account_id[0] if account_id else None,
            'AccountDescription': description[0] if description else None,
            'StandardAccountID': standard_account_id[0] if standard_account_id else None,
            'AccountType': account_type[0] if account_type else None,
            'AccountCreationDate': creation_date[0] if creation_date else None,
            'OpeningCreditBalance': opening_credit[0] if opening_credit else None,
            'ClosingCreditBalance': closing_credit[0] if closing_credit else None
        })

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)
    return df

    

def parse_customers(xml_content: str) -> pd.DataFrame:
    """
    <nsSAFT:Customers>
			<nsSAFT:Customer><nsSAFT:CompanyStructure><nsSAFT:RegistrationNumber>0031680233</nsSAFT:RegistrationNumber><nsSAFT:Name>SOFT GALAXY INTERNATIONAL SRL</nsSAFT:Name><nsSAFT:Address><nsSAFT:City>BUCURESTI SECTOR 3</nsSAFT:City><nsSAFT:PostalCode>-</nsSAFT:PostalCode><nsSAFT:Region>RO-B</nsSAFT:Region><nsSAFT:Country>RO</nsSAFT:Country><nsSAFT:AddressType>PostalAddress</nsSAFT:AddressType></nsSAFT:Address></nsSAFT:CompanyStructure><nsSAFT:CustomerID>0031680233</nsSAFT:CustomerID><nsSAFT:SelfBillingIndicator>0</nsSAFT:SelfBillingIndicator><nsSAFT:AccountID>411100001</nsSAFT:AccountID><nsSAFT:OpeningDebitBalance>42645.51</nsSAFT:OpeningDebitBalance><nsSAFT:ClosingDebitBalance>44777.78</nsSAFT:ClosingDebitBalance></nsSAFT:Customer>
			<nsSAFT:Customer><nsSAFT:CompanyStructure><nsSAFT:RegistrationNumber>01SK212005936</nsSAFT:RegistrationNumber><nsSAFT:Name>DATARYTHM S.R.O.</nsSAFT:Name><nsSAFT:Address><nsSAFT:City>KOSICKY</nsSAFT:City><nsSAFT:PostalCode>-</nsSAFT:PostalCode><nsSAFT:Country>SK</nsSAFT:Country><nsSAFT:AddressType>PostalAddress</nsSAFT:AddressType></nsSAFT:Address></nsSAFT:CompanyStructure><nsSAFT:CustomerID>01SK212005936</nsSAFT:CustomerID><nsSAFT:SelfBillingIndicator>0</nsSAFT:SelfBillingIndicator><nsSAFT:AccountID>411100002</nsSAFT:AccountID><nsSAFT:OpeningDebitBalance>80437.92</nsSAFT:OpeningDebitBalance><nsSAFT:ClosingDebitBalance>40218.96</nsSAFT:ClosingDebitBalance></nsSAFT:Customer>
			<nsSAFT:Customer><nsSAFT:CompanyStructure><nsSAFT:RegistrationNumber>01BG3074944468</nsSAFT:RegistrationNumber><nsSAFT:Name>INFITECH SOFTWARE LTD</nsSAFT:Name><nsSAFT:Address><nsSAFT:StreetName>D FLOOR 5 OFFICE 26-27</nsSAFT:StreetName><nsSAFT:City>Sofia</nsSAFT:City><nsSAFT:PostalCode>-</nsSAFT:PostalCode><nsSAFT:Country>BG</nsSAFT:Country><nsSAFT:AddressType>PostalAddress</nsSAFT:AddressType></nsSAFT:Address></nsSAFT:CompanyStructure><nsSAFT:CustomerID>01BG3074944468</nsSAFT:CustomerID><nsSAFT:SelfBillingIndicator>0</nsSAFT:SelfBillingIndicator><nsSAFT:AccountID>411100003</nsSAFT:AccountID><nsSAFT:OpeningDebitBalance>38458.39</nsSAFT:OpeningDebitBalance><nsSAFT:ClosingDebitBalance>76916.78</nsSAFT:ClosingDebitBalance></nsSAFT:Customer>
			</nsSAFT:Customers>
    """
    root = etree.parse(xml_content)

    # Extract the Customer entries
    customer_entries = root.xpath("//nsSAFT:Customers/nsSAFT:Customer", namespaces=NAMESPACES)

    # Prepare an empty list to store data for DataFrame
    data = []

    # Loop through each Customer and extract relevant fields
    for entry in customer_entries:
        registration_number = entry.xpath(".//nsSAFT:RegistrationNumber/text()", namespaces=NAMESPACES)
        name = entry.xpath(".//nsSAFT:Name/text()", namespaces=NAMESPACES)
        city = entry.xpath(".//nsSAFT:City/text()", namespaces=NAMESPACES)
        postal_code = entry.xpath(".//nsSAFT:PostalCode/text()", namespaces=NAMESPACES)
        country = entry.xpath(".//nsSAFT:Country/text()", namespaces=NAMESPACES)
        customer_id = entry.xpath("nsSAFT:CustomerID/text()", namespaces=NAMESPACES)
        account_id = entry.xpath("nsSAFT:AccountID/text()", namespaces=NAMESPACES)
        opening_debit = entry.xpath("nsSAFT:OpeningDebitBalance/text()", namespaces=NAMESPACES)
        closing_debit = entry.xpath("nsSAFT:ClosingDebitBalance/text()", namespaces=NAMESPACES)

        # Add extracted data to the list
        data.append({
            'RegistrationNumber': registration_number[0] if registration_number else None,
            'Name': name[0] if name else None,
            'City': city[0] if city else None,
            'PostalCode': postal_code[0] if postal_code else None, 
            'Country': country[0] if country else None,
            'CustomerID': customer_id[0] if customer_id else None,
            'AccountID': account_id[0] if account_id else None,
            'OpeningDebitBalance': opening_debit[0] if opening_debit else None,
            'ClosingDebitBalance': closing_debit[0] if closing_debit else None
        })

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)
    return df

def parse_suppliers(xml_content: str) -> pd.DataFrame:
    """
    <nsSAFT:Suppliers>
			<nsSAFT:Supplier><nsSAFT:CompanyStructure><nsSAFT:RegistrationNumber>0031680233</nsSAFT:RegistrationNumber><nsSAFT:Name>SOFT GALAXY INTERNATIONAL SRL</nsSAFT:Name><nsSAFT:Address><nsSAFT:City>BUCURESTI SECTOR 3</nsSAFT:City><nsSAFT:PostalCode>-</nsSAFT:PostalCode><nsSAFT:Region>RO-B</nsSAFT:Region><nsSAFT:Country>RO</nsSAFT:Country><nsSAFT:AddressType>PostalAddress</nsSAFT:AddressType></nsSAFT:Address></nsSAFT:CompanyStructure><nsSAFT:SupplierID>0031680233</nsSAFT:SupplierID><nsSAFT:SelfBillingIndicator>0</nsSAFT:SelfBillingIndicator><nsSAFT:AccountID>411100001</nsSAFT:AccountID><nsSAFT:OpeningDebitBalance>42645.51</nsSAFT:OpeningDebitBalance><nsSAFT:ClosingDebitBalance>44777.78</nsSAFT:ClosingDebitBalance></nsSAFT:Supplier>
    </nsSAFT:Suppliers>
    """
    root = etree.parse(xml_content)

    # Extract the Supplier entries
    supplier_entries = root.xpath("//nsSAFT:Suppliers/nsSAFT:Supplier", namespaces=NAMESPACES)

    # Prepare an empty list to store data for DataFrame
    data = []

    # Loop through each Supplier and extract relevant fields
    for entry in supplier_entries:
        registration_number = entry.xpath(".//nsSAFT:RegistrationNumber/text()", namespaces=NAMESPACES)
        name = entry.xpath(".//nsSAFT:Name/text()", namespaces=NAMESPACES)
        city = entry.xpath(".//nsSAFT:City/text()", namespaces=NAMESPACES)
        postal_code = entry.xpath(".//nsSAFT:PostalCode/text()", namespaces=NAMESPACES)
        country = entry.xpath(".//nsSAFT:Country/text()", namespaces=NAMESPACES)
        supplier_id = entry.xpath("nsSAFT:SupplierID/text()", namespaces=NAMESPACES)
        account_id = entry.xpath("nsSAFT:AccountID/text()", namespaces=NAMESPACES)
        opening_debit = entry.xpath("nsSAFT:OpeningDebitBalance/text()", namespaces=NAMESPACES)
        closing_debit = entry.xpath("nsSAFT:ClosingDebitBalance/text()", namespaces=NAMESPACES)

        # Add extracted data to the list
        data.append({
            'RegistrationNumber': registration_number[0] if registration_number else None,
            'Name': name[0] if name else None,
            'City': city[0] if city else None,
            'PostalCode': postal_code[0] if postal_code else None,
            'Country': country[0] if country else None,
            'SupplierID': supplier_id[0] if supplier_id else None,
            'AccountID': account_id[0] if account_id else None,
            'OpeningDebitBalance': opening_debit[0] if opening_debit else None,
            'ClosingDebitBalance': closing_debit[0] if closing_debit else None
        })

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)
    return df


def parse_remaining_fields(xml_content: str) -> pd.DataFrame:
    """
    <nsSAFT:UOMTable>
			<nsSAFT:UOMTableEntry><nsSAFT:UnitOfMeasure>H87</nsSAFT:UnitOfMeasure><nsSAFT:Description>Bucata</nsSAFT:Description></nsSAFT:UOMTableEntry>
			</nsSAFT:UOMTable>
		<nsSAFT:AnalysisTypeTable>
			<nsSAFT:AnalysisTypeTableEntry><nsSAFT:AnalysisType>A</nsSAFT:AnalysisType><nsSAFT:AnalysisTypeDescription>Activitate</nsSAFT:AnalysisTypeDescription><nsSAFT:AnalysisID>0000</nsSAFT:AnalysisID><nsSAFT:AnalysisIDDescription>OPERATIUNI NEINCADRATE SAF-T</nsSAFT:AnalysisIDDescription></nsSAFT:AnalysisTypeTableEntry>
			</nsSAFT:AnalysisTypeTable>
		<nsSAFT:MovementTypeTable>
			</nsSAFT:MovementTypeTable>
		<nsSAFT:Products>
			<nsSAFT:Product><nsSAFT:ProductCode>COD_GENERIC</nsSAFT:ProductCode><nsSAFT:GoodsServicesID>01</nsSAFT:GoodsServicesID><nsSAFT:Description>VANZARE</nsSAFT:Description><nsSAFT:ProductCommodityCode>0</nsSAFT:ProductCommodityCode><nsSAFT:ValuationMethod>FIFO</nsSAFT:ValuationMethod><nsSAFT:UOMBase>H87</nsSAFT:UOMBase><nsSAFT:UOMStandard>H87</nsSAFT:UOMStandard><nsSAFT:UOMToUOMBaseConversionFactor>1</nsSAFT:UOMToUOMBaseConversionFactor></nsSAFT:Product>
			</nsSAFT:Products>
		<nsSAFT:Owners>
			</nsSAFT:Owners>
		<nsSAFT:Assets/>
    """
    
    return pd.DataFrame()

def parse_transactions(xml_content: str) -> pd.DataFrame:
    """
    </nsSAFT:Transaction><nsSAFT:Transaction>
			<nsSAFT:TransactionID>1620</nsSAFT:TransactionID><nsSAFT:Period>3</nsSAFT:Period><nsSAFT:PeriodYear>2025</nsSAFT:PeriodYear><nsSAFT:TransactionDate>2025-03-17</nsSAFT:TransactionDate><nsSAFT:Description>Numar document: EC03 - IMPOZITUL PE VENITURI DE NATURA SALARIILOR</nsSAFT:Description><nsSAFT:BatchID>1620</nsSAFT:BatchID><nsSAFT:SystemEntryDate>2025-03-17</nsSAFT:SystemEntryDate><nsSAFT:GLPostingDate>2025-03-17</nsSAFT:GLPostingDate><nsSAFT:CustomerID>0047891725</nsSAFT:CustomerID><nsSAFT:SupplierID>0047891725</nsSAFT:SupplierID><nsSAFT:SystemID>1620</nsSAFT:SystemID><nsSAFT:TransactionLine><nsSAFT:RecordID>91</nsSAFT:RecordID><nsSAFT:AccountID>444</nsSAFT:AccountID><nsSAFT:Analysis><nsSAFT:AnalysisType>A</nsSAFT:AnalysisType><nsSAFT:AnalysisID>0000</nsSAFT:AnalysisID><nsSAFT:AnalysisAmount><nsSAFT:Amount>264.00</nsSAFT:Amount><nsSAFT:CurrencyCode>RON</nsSAFT:CurrencyCode><nsSAFT:CurrencyAmount>264.00</nsSAFT:CurrencyAmount><nsSAFT:ExchangeRate>1.0000</nsSAFT:ExchangeRate></nsSAFT:AnalysisAmount></nsSAFT:Analysis><nsSAFT:CustomerID>0047891725</nsSAFT:CustomerID><nsSAFT:SupplierID>0047891725</nsSAFT:SupplierID><nsSAFT:Description>IMPOZITUL PE VENITURI DE NATURA SALARIILOR</nsSAFT:Description><nsSAFT:DebitAmount><nsSAFT:Amount>264.00</nsSAFT:Amount><nsSAFT:CurrencyCode>RON</nsSAFT:CurrencyCode><nsSAFT:CurrencyAmount>264.00</nsSAFT:CurrencyAmount><nsSAFT:ExchangeRate>1.0000</nsSAFT:ExchangeRate></nsSAFT:DebitAmount><nsSAFT:TaxInformation><nsSAFT:TaxType>000</nsSAFT:TaxType><nsSAFT:TaxCode>000000</nsSAFT:TaxCode><nsSAFT:TaxAmount><nsSAFT:Amount>0.00</nsSAFT:Amount><nsSAFT:CurrencyCode>RON</nsSAFT:CurrencyCode><nsSAFT:CurrencyAmount>0.00</nsSAFT:CurrencyAmount><nsSAFT:ExchangeRate>1.0000</nsSAFT:ExchangeRate></nsSAFT:TaxAmount></nsSAFT:TaxInformation></nsSAFT:TransactionLine><nsSAFT:TransactionLine><nsSAFT:RecordID>92</nsSAFT:RecordID><nsSAFT:AccountID>512100001</nsSAFT:AccountID><nsSAFT:Analysis><nsSAFT:AnalysisType>A</nsSAFT:AnalysisType><nsSAFT:AnalysisID>0000</nsSAFT:AnalysisID><nsSAFT:AnalysisAmount><nsSAFT:Amount>264.00</nsSAFT:Amount><nsSAFT:CurrencyCode>RON</nsSAFT:CurrencyCode><nsSAFT:CurrencyAmount>264.00</nsSAFT:CurrencyAmount><nsSAFT:ExchangeRate>1.0000</nsSAFT:ExchangeRate></nsSAFT:AnalysisAmount></nsSAFT:Analysis><nsSAFT:CustomerID>0047891725</nsSAFT:CustomerID><nsSAFT:SupplierID>0047891725</nsSAFT:SupplierID><nsSAFT:Description>IMPOZITUL PE VENITURI DE NATURA SALARIILOR</nsSAFT:Description><nsSAFT:CreditAmount><nsSAFT:Amount>264.00</nsSAFT:Amount><nsSAFT:CurrencyCode>RON</nsSAFT:CurrencyCode><nsSAFT:CurrencyAmount>264.00</nsSAFT:CurrencyAmount><nsSAFT:ExchangeRate>1.0000</nsSAFT:ExchangeRate></nsSAFT:CreditAmount><nsSAFT:TaxInformation><nsSAFT:TaxType>000</nsSAFT:TaxType><nsSAFT:TaxCode>000000</nsSAFT:TaxCode><nsSAFT:TaxAmount><nsSAFT:Amount>0.00</nsSAFT:Amount><nsSAFT:CurrencyCode>RON</nsSAFT:CurrencyCode><nsSAFT:CurrencyAmount>0.00</nsSAFT:CurrencyAmount><nsSAFT:ExchangeRate>1.0000</nsSAFT:ExchangeRate></nsSAFT:TaxAmount></nsSAFT:TaxInformation></nsSAFT:TransactionLine>
    """
    
    # Initialize empty list to store transaction data
    data = []

    # Parse the XML content
    root = etree.parse(xml_content)

    # Find all Transaction elements
    transactions = root.xpath("//nsSAFT:Transaction", namespaces=NAMESPACES)

    # Iterate through each transaction
    for transaction in transactions:
        # Extract transaction header data
        transaction_id = transaction.xpath("nsSAFT:TransactionID/text()", namespaces=NAMESPACES)
        period = transaction.xpath("nsSAFT:Period/text()", namespaces=NAMESPACES)
        period_year = transaction.xpath("nsSAFT:PeriodYear/text()", namespaces=NAMESPACES)
        transaction_date = transaction.xpath("nsSAFT:TransactionDate/text()", namespaces=NAMESPACES)
        description = transaction.xpath("nsSAFT:Description/text()", namespaces=NAMESPACES)
        batch_id = transaction.xpath("nsSAFT:BatchID/text()", namespaces=NAMESPACES)
        system_entry_date = transaction.xpath("nsSAFT:SystemEntryDate/text()", namespaces=NAMESPACES)
        gl_posting_date = transaction.xpath("nsSAFT:GLPostingDate/text()", namespaces=NAMESPACES)
        customer_id = transaction.xpath("nsSAFT:CustomerID/text()", namespaces=NAMESPACES)
        supplier_id = transaction.xpath("nsSAFT:SupplierID/text()", namespaces=NAMESPACES)
        system_id = transaction.xpath("nsSAFT:SystemID/text()", namespaces=NAMESPACES)

        # Get transaction lines
        transaction_lines = transaction.xpath("nsSAFT:TransactionLine", namespaces=NAMESPACES)
        for line in transaction_lines:
            record_id = line.xpath("nsSAFT:RecordID/text()", namespaces=NAMESPACES)
            account_id = line.xpath("nsSAFT:AccountID/text()", namespaces=NAMESPACES)
            line_description = line.xpath("nsSAFT:Description/text()", namespaces=NAMESPACES)
            
            # Get amounts
            debit_amount = line.xpath(".//nsSAFT:DebitAmount/nsSAFT:Amount/text()", namespaces=NAMESPACES)
            credit_amount = line.xpath(".//nsSAFT:CreditAmount/nsSAFT:Amount/text()", namespaces=NAMESPACES)
            
            # Get tax information
            tax_type = line.xpath(".//nsSAFT:TaxType/text()", namespaces=NAMESPACES)
            tax_code = line.xpath(".//nsSAFT:TaxCode/text()", namespaces=NAMESPACES)
            tax_amount = line.xpath(".//nsSAFT:TaxAmount/nsSAFT:Amount/text()", namespaces=NAMESPACES)

            # Add transaction data to list
            data.append({
                'TransactionID': transaction_id[0] if transaction_id else None,
                'Period': period[0] if period else None,
                'PeriodYear': period_year[0] if period_year else None,
                'TransactionDate': transaction_date[0] if transaction_date else None,
                'Description': description[0] if description else None,
                'BatchID': batch_id[0] if batch_id else None,
                'SystemEntryDate': system_entry_date[0] if system_entry_date else None,
                'GLPostingDate': gl_posting_date[0] if gl_posting_date else None,
                'CustomerID': customer_id[0] if customer_id else None,
                'SupplierID': supplier_id[0] if supplier_id else None,
                'SystemID': system_id[0] if system_id else None,
                'RecordID': record_id[0] if record_id else None,
                'AccountID': account_id[0] if account_id else None,
                'LineDescription': line_description[0] if line_description else None,
                'DebitAmount': float(debit_amount[0]) if debit_amount else 0.0,
                'CreditAmount': float(credit_amount[0]) if credit_amount else 0.0,
                'TaxType': tax_type[0] if tax_type else None,
                'TaxCode': tax_code[0] if tax_code else None,
                'TaxAmount': float(tax_amount[0]) if tax_amount else 0.0
            })

    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(data)
    return df
   
    
def parse_saft_to_excel(xml_content: str) -> bool:
    """Parse SAFT XML content and write multiple dataframes to Excel file.
    
    Args:
        xml_content (str): XML content as string
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Parse all sections
        tax_tables_df = parse_tax_tables(xml_content)
        gl_accounts_df = parse_general_ledger_accounts(xml_content) 
        customers_df = parse_customers(xml_content)
        suppliers_df = parse_suppliers(xml_content)
        transactions_df = parse_transactions(xml_content)

        # Create Excel writer object
        with pd.ExcelWriter('saft_data.xlsx') as writer:
            # Write each dataframe to a separate sheet
            tax_tables_df.to_excel(writer, sheet_name='Tax Tables', index=False)
            gl_accounts_df.to_excel(writer, sheet_name='GL Accounts', index=False)
            customers_df.to_excel(writer, sheet_name='Customers', index=False)
            suppliers_df.to_excel(writer, sheet_name='Suppliers', index=False)
            transactions_df.to_excel(writer, sheet_name='Transactions', index=False)

        return True

    except Exception as e:
        print(f"Error writing to Excel: {str(e)}")
        return False
    


if __name__ == "__main__":
    # Read the XML file
    xml_path = "../../../saft_example.XML"

    parse_saft_to_excel(xml_path)
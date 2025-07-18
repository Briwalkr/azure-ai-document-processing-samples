from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Currency(BaseModel):
    """
    A class representing a currency in a form.
    """

    currency_code: Optional[str] = Field(
        description='Currency code, e.g. USD'
    )
    amount: Optional[float] = Field(
        description='Currency amount, e.g. $100.00'
    )


class Address(BaseModel):
    """
    A class representing an address in a form.
    """

    street: Optional[str] = Field(
        description='Street address, e.g. 123 456th St.'
    )
    city: Optional[str] = Field(
        description='Name of city, town, village, etc., e.g. New York'
    )
    state: Optional[str] = Field(
        description='Name of State or local administrative division, e.g. NY'
    )
    postal_code: Optional[str] = Field(
        description='Postal code, e.g. 10001'
    )
    country: Optional[str] = Field(
        description='Country, e.g. USA'
    )


class Signature(BaseModel):
    """
    A class representing a signature for the Authorized Representative on the form.
    """

    signatory: Optional[str] = Field(
        description='Name of the person who signed the invoice, e.g. John Doe'
    )

    has_written_signature: Optional[bool] = Field(
        description='Indicates if the invoice has a written signature, e.g. true'
    )

class Acord25(BaseModel):
    """
    A class representing a Certificate Of Liability Insurance (ACORD 25) form.
    """

    certificate_date: Optional[str] = Field(
        description='Date the Certificate of Liability Insurance was issued, e.g., 11/15/2020'
    )
    producer_name: Optional[str] = Field(
        description='Name of the producer generating the form, e.g. Microsoft Corp'
    )
    producer_address: Optional[Address] = Field(
        description='Full mailing address of the producer, e.g. 123 Other St., Redmond, WA, 98052, USA'
    )
    insured_name: Optional[str] = Field(
        description='Name of the insured party, e.g. XYZ Corp'
    )
    insured_address: Optional[Address] = Field(
        description='Full mailing address of the insured party, e.g. 456 Insured St., Redmond, WA, 98052, USA'
    )
    insurer_affording_coverage_a: Optional[str] = Field(
        description='Name of the insurer providing coverage A, e.g. Some Insurance Co.'
    )
    insurer_affording_coverage_a_naic: Optional[str] = Field(
        description='NAIC number of the insurer providing coverage A, e.g. 12345'
    )
    insurer_affording_coverage_b: Optional[str] = Field(
        description='Name of the insurer providing coverage A, e.g. Some Insurance Co.'
    )
    insurer_affording_coverage_b_naic: Optional[str] = Field(
        description='NAIC number of the insurer providing coverage A, e.g. 12345'
    )
    insurer_affording_coverage_c: Optional[str] = Field(
        description='Name of the insurer providing coverage A, e.g. Some Insurance Co.'
    )
    insurer_affording_coverage_c_naic: Optional[str] = Field(
        description='NAIC number of the insurer providing coverage A, e.g. 12345'
    )
    insurer_affording_coverage_d: Optional[str] = Field(
        description='Name of the insurer providing coverage A, e.g. Some Insurance Co.'
    )
    insurer_affording_coverage_d_naic: Optional[str] = Field(
        description='NAIC number of the insurer providing coverage A, e.g. 12345'
    )
    insurer_affording_coverage_e: Optional[str] = Field(
        description='Name of the insurer providing coverage A, e.g. Some Insurance Co.'
    )
    insurer_affording_coverage_e_naic: Optional[str] = Field(
        description='NAIC number of the insurer providing coverage A, e.g. 12345'
    )
    insurer_affording_coverage_f: Optional[str] = Field(
        description='Name of the insurer providing coverage A, e.g. Some Insurance Co.'
    )
    insurer_affording_coverage_f_naic: Optional[str] = Field(
        description='NAIC number of the insurer providing coverage A, e.g. 12345'
    )
    certificate_number: Optional[str] = Field(
        description='Certificate number, e.g. 1234'
    )
    revision_number: Optional[str] = Field(
        description='Revision number of the certificate, e.g. 1'
    )
    invoice_id: Optional[str] = Field(
        description='Reference ID or invoice number for the invoice, e.g. INV-100'
    )
    authorized_signature: Optional[Signature] = Field(
        description='Signature of the Authorized Representative, e.g. John Doe'
    )

from enum import Enum

import polars as pl

DEFAULT_FOCUS_NAMESPACE = "F"


class FocusColumnNames(Enum):
    """
    Focus column names as described in https://focus.finops.org/#specification
    """

    PLACE_HOLDER = "PlaceHolder"

    CHARGE_PERIOD_START = "ChargePeriodStart"
    CHARGE_PERIOD_END = "ChargePeriodEnd"
    CHARGE_FREQUENCY = "ChargeFrequency"
    CHARGE_DESCRIPTION = "ChargeDescription"
    CHARGE_CATEGORY = "ChargeCategory"

    BILLING_PERIOD_START = "BillingPeriodStart"
    BILLING_PERIOD_END = "BillingPeriodEnd"

    PROVIDER = "Provider"
    PUBLISHER = "Publisher"
    INVOICE_ISSUER = "InvoiceIssuer"

    BILLING_ACCOUNT_ID = "BillingAccountId"
    BILLING_ACCOUNT_NAME = "BillingAccountName"

    BILLED_COST = "BilledCost"
    BILLING_CURRENCY = "BillingCurrency"
    EFFECTIVE_COST = "EffectiveCost"

    REGION = "RegionId"
    # RegionName introduced in 1.0: https://focus.finops.org/focus-columns/?prod_focus_columns%5Bquery%5D=region&prod_focus_columns%5BrefinementList%5D%5Bcategories%5D%5B0%5D=Location#modal-column-14473
    REGION_NAME = "RegionName"

    SERVICE_CATEGORY = "ServiceCategory"
    SERVICE_NAME = "ServiceName"

    SUB_ACCOUNT_NAME = "SubAccountName"
    SUB_ACCOUNT_ID = "SubAccountId"

    AVAILABILITY_ZONE = "AvailabilityZone"

    RESOURCE_NAME = "ResourceName"
    RESOURCE_ID = "ResourceId"
    RESOURCE_TYPE = "ResourceType"

    COMMITMENT_DISCOUNT_NAME = "CommitmentDiscountName"
    COMMITMENT_DISCOUNT_ID = "CommitmentDiscountId"
    COMMITMENT_DISCOUNT_TYPE = "CommitmentDiscountType"
    COMMITMENT_DISCOUNT_CATEGORY = "CommitmentDiscountCategory"

    PRICING_QUANTITY = "PricingQuantity"
    PRICING_UNIT = "PricingUnit"
    PRICING_CATEGORY = "PricingCategory"

    SKU_ID = "SkuId"
    SKU_PRICE_ID = "SkuPriceId"

    LIST_UNIT_PRICE = "ListUnitPrice"
    LIST_COST = "ListCost"

    CONSUMED_QUANTITY = "ConsumedQuantity"
    CONSUMED_UNIT = "ConsumedUnit"

    # ContractedCost introduced in 1.0: https://focus.finops.org/focus-columns/?prod_focus_columns%5Bquery%5D=Contracted#modal-column-14451
    CONTRACTED_COST = "ContractedCost"
    # ContractedUnitPrice introduced in 1.0: https://focus.finops.org/focus-columns/?prod_focus_columns%5Bquery%5D=Contracted#modal-column-14453
    CONTRACTED_UNIT_PRICE = "ContractedUnitPrice"


FOCUS_DATETIME_ISO_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def get_dtype_for_focus_column_name(focus_column_name: FocusColumnNames):
    """
    Return the dtype for the focus column name
    """

    # convert loop to match statements
    if focus_column_name == FocusColumnNames.PLACE_HOLDER:
        raise ValueError("PLACE_HOLDER is not a valid focus column name")
    elif (
        focus_column_name == FocusColumnNames.CHARGE_PERIOD_START
        or focus_column_name == FocusColumnNames.CHARGE_PERIOD_END
        or focus_column_name == FocusColumnNames.BILLING_PERIOD_START
        or focus_column_name == FocusColumnNames.BILLING_PERIOD_END
    ):
        return pl.Datetime
    elif (
        focus_column_name == FocusColumnNames.BILLED_COST
        or focus_column_name == FocusColumnNames.EFFECTIVE_COST
        or focus_column_name == FocusColumnNames.LIST_COST
        or focus_column_name == FocusColumnNames.LIST_UNIT_PRICE
        or focus_column_name == FocusColumnNames.PRICING_QUANTITY
        or focus_column_name == FocusColumnNames.CONSUMED_QUANTITY
    ):
        return pl.Float64
    else:
        return pl.Utf8

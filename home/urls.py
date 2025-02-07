from django.urls import path
from .views import (
    CreateMemberApiView,
    CreateNomineeApiView,
    CreateFinancialInfoApiView,
    CreateMemberLifeStyleApiView,
    ProductSearchApiView,
    CreateQuoteApiView,
    SaveApplicationApiView,
    PayoutDetailsApiView,
    CreatePaymentDetailsApiView,
    GetAllPlanApiView,
    GetAllProductByPlanNoApiView,
    GetFrequencyApiView,
    GetDurationsApiView,
    CustomerSearchApiView,
    GetPremiumLimitsApiView,
    CreatePayoutModeApiView,
    IdentificationDetailsApiView,
    DocumentsUploadApiView,
    PayerDetailsApiView,
    InitialPaymentDetailsApiView,
    PaymentDetailsApiView,
    GenerateApplicationIdApiView,
    InsuredDetailsApiView,
    UpdateFinancialInfoApiView,
    SubmitMedicalsApiView,
    SubmitAdditionalMedicalsApiView,
    BeneficiaryDetailsApiView,
    NomineeDetailsApiView,
    SubSequentPaymentApiView,
    FinalSubmissionCaseApplicationApiView,
    AsCodeRelationshipsApiView,
    AsCodeBritamOccupationApiView,
    AsCodeClientPrefixApiView,
    AsCodeMaritalStatusApiView,
    GetClientsApiView,
    GetCaseApiView,
    GetFilterbyAgentIdApiView,
    GetProcessPartialApiView,
    GetPartialDetailsApiView,
    UpdatePayoutApiView,
    GetMonthlyStatementsApiView,
    GetTaxCertificateApiView,
    PremiumRenewalApiView,
    GetBankAccountsApiView,
    GetBeneficiaryApiView,
    GetBankAccountPoliciesApiView,
    GetPolicyDetailsApiView,
    GetBenefitsApiView
)

app_name = "home"


urlpatterns = [
    path("filter/agent-id/",GetFilterbyAgentIdApiView.as_view()),
    path("get-case/", GetCaseApiView.as_view(), name="get-case"),
    path("create-member/", CreateMemberApiView.as_view(), name="create-member"),
    path("create-nominee/", CreateNomineeApiView.as_view(), name="create-nominee"),
    path("create-financial-info/", CreateFinancialInfoApiView.as_view(), name="create-financial-info"),
    path("create-member-lifestyle/", CreateMemberLifeStyleApiView.as_view(), name="create-member-lifestyle"),
    path("product-search/", ProductSearchApiView.as_view(), name="product-search"),
    path("create-quote/", CreateQuoteApiView.as_view(), name="create-quote"),
    path("save-application/", SaveApplicationApiView.as_view(), name="save-application"),
    path("payout-details/", PayoutDetailsApiView.as_view(), name="payout-details"),
    path("create-payment-details/", CreatePaymentDetailsApiView.as_view(), name="create-payment-details"),
    path("get-all-plan/", GetAllPlanApiView.as_view(), name="get-all-plan"),
    path("get-all-product-by-plan-no/", GetAllProductByPlanNoApiView.as_view(), name="get-all-product-by-plan-no"),
    path("get-frequency/", GetFrequencyApiView.as_view(), name="get-frequency"),
    path("get-clients/",GetClientsApiView.as_view(),name="api-get-clients"),
    path("get-durations/", GetDurationsApiView.as_view(), name="get-durations"),
    path("customer-search/", CustomerSearchApiView.as_view(), name="customer-search"),
    path("get-premium-limits/", GetPremiumLimitsApiView.as_view(), name="get-premium-limits"),
    path("create-payout-mode/", CreatePayoutModeApiView.as_view(), name="create-payout-mode"),
    path("identification-details/", IdentificationDetailsApiView.as_view(), name="identification-details"),
    path("documents-upload/", DocumentsUploadApiView.as_view(), name="documents-upload"),
    path("payer-details/", PayerDetailsApiView.as_view(), name="payer-details"),
    path("initial-payment-details/", InitialPaymentDetailsApiView.as_view(), name="initial-payment-details"),
    path("payment-details/", PaymentDetailsApiView.as_view(), name="payment-details"),
    path("generate-application-id/", GenerateApplicationIdApiView.as_view(), name="generate-application-id"),
    path("insured-details/", InsuredDetailsApiView.as_view(), name="insured-details"),
    path("update-financial-info/", UpdateFinancialInfoApiView.as_view(), name="update-financial-info"),
    path("submit-medicals/", SubmitMedicalsApiView.as_view(), name="submit-medicals"),
    path("submit-additional-medicals/", SubmitAdditionalMedicalsApiView.as_view(), name="submit-additional-medicals"),
    path("beneficiary-details/", BeneficiaryDetailsApiView.as_view(), name="beneficiary-details"),
    path("nominee-details/", NomineeDetailsApiView.as_view(), name="nominee-details"),
     path("subsequent-payment/", SubSequentPaymentApiView.as_view(), name="subsequent-payment"),
     path(
        "final-submission-case-application/",
        FinalSubmissionCaseApplicationApiView.as_view(),
        name="final-submission-case-application",
    ),
     path(
        "as-code-relationships/",
        AsCodeRelationshipsApiView.as_view(),
        name="as-code-relationships",
    ),
      path(
        "as-code-britam-occupation/",
        AsCodeBritamOccupationApiView.as_view(),
        name="as-code-britam-occupation",
    ),
    path(
        "as-code-client-prefix/",
        AsCodeClientPrefixApiView.as_view(),
        name="as-code-client-prefix",
    ),
    path(
        "as-code-marital-status/",
        AsCodeMaritalStatusApiView.as_view(),
        name="as-code-marital-status",
    ),




    path(
        "process-partial/",
        GetProcessPartialApiView.as_view()
    ),
    path(
        "get-partial-details/",
        GetPartialDetailsApiView.as_view()
    ),
    path(
        "update-payout/",
        UpdatePayoutApiView.as_view()
        ),
    path(
        "get-monthly-statements/",
        GetMonthlyStatementsApiView.as_view()
    ),
    path(
        "get-tax-certificate/",
        GetTaxCertificateApiView.as_view()
    ),
    path(
        "premium-renewal/",
        PremiumRenewalApiView.as_view()
    ),
    path(
        "bank-accounts/",
        GetBankAccountsApiView.as_view()
    ),
    path(
        "get-beneficiaries/",
        GetBeneficiaryApiView.as_view()
    ),
    path (
        "get-bank-account-policies/",
        GetBankAccountPoliciesApiView.as_view()
    ),
    path(
        "get-policy-details/",
        GetPolicyDetailsApiView.as_view()
    ),
    path(
        "get-benefits/",
        GetBenefitsApiView.as_view()
    )

]

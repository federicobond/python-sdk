import typing

from open_feature.evaluation_context import EvaluationContext
from open_feature.flag_evaluation import FlagResolutionDetails, Reason
from open_feature.hooks.hook import Hook
from open_feature.provider.metadata import Metadata
from open_feature.provider.no_op_metadata import NoOpMetadata
from open_feature.provider.provider import AbstractProvider

PASSED_IN_DEFAULT = "Passed in default"


class NoOpProvider(AbstractProvider):
    def get_metadata(self) -> Metadata:
        return NoOpMetadata()

    def get_provider_hooks(self) -> typing.List[Hook]:
        return []

    def resolve_boolean_details(
        self,
        flag_key: str,
        default_value: bool,
        evaluation_context: typing.Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[bool]:
        return FlagResolutionDetails(
            value=default_value,
            reason=Reason.DEFAULT,
            variant=PASSED_IN_DEFAULT,
        )

    def resolve_string_details(
        self,
        flag_key: str,
        default_value: str,
        evaluation_context: typing.Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[str]:
        return FlagResolutionDetails(
            value=default_value,
            reason=Reason.DEFAULT,
            variant=PASSED_IN_DEFAULT,
        )

    def resolve_integer_details(
        self,
        flag_key: str,
        default_value: int,
        evaluation_context: typing.Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[int]:
        return FlagResolutionDetails(
            value=default_value,
            reason=Reason.DEFAULT,
            variant=PASSED_IN_DEFAULT,
        )

    def resolve_float_details(
        self,
        flag_key: str,
        default_value: float,
        evaluation_context: typing.Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[float]:
        return FlagResolutionDetails(
            value=default_value,
            reason=Reason.DEFAULT,
            variant=PASSED_IN_DEFAULT,
        )

    def resolve_object_details(
        self,
        flag_key: str,
        default_value: typing.Union[dict, list],
        evaluation_context: typing.Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[typing.Union[dict, list]]:
        return FlagResolutionDetails(
            value=default_value,
            reason=Reason.DEFAULT,
            variant=PASSED_IN_DEFAULT,
        )

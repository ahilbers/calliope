from calliope import __version__ as CALLIOPE_VERSION

from typing import Callable, Dict, Sequence, get_type_hints, TypeVar

from pydantic import validator, ValidationError
from datetime import datetime
from dateutil import parser


__all__ = ["range_check", "objective_options_validation", "calliope_version_validation", "timeseries_dateformat_validation"]

Comparable_t = TypeVar("Comparable_t", int, float, datetime)

# TODO: rewrite as a simple function, where the parameters are injected into
# the closure in a generic factory method
def range_check(cls, _max, values, *, min_key):
    """Validator function for a range config object"""
    if min_key in values and values[min_key] > _max:
        raise ValueError(f"bad range: {values[min_key]} > {_max}")
    return _max


def objective_options_validation(cls, _objective, values):
    """
    'cost_class' and 'sense' need to be defined if run.objective is 'minmax_cost_optimisation'
    """
    if _objective == 'minmax_cost_optimization':
        if "cost_class" not in values or "sense" not in values:
            return ValueError("minmax_cost_optimisation chosen with either cost_class or sense undefined")
    return _objective


# def operate_options_validation():
#     """
#     Operate options are only read if mode = 'operate'.
#     NOTE: not sure this needs to actually exist
#     """


# def backend_validation(key, keys, **opts):
#     """
#     If backend == 'pyomo', 'solver', 'solver_io' and 'solver_options' can be defined. If (at some point) backend == gurobi, only 'solver_options' can be defined.
#     """
#     @validator(key, **opts)
#     def _backend_validation(cls, _backend_options, values):
#         allowed_opts = {
#             'gurobi': ['solver_options']
#             'pyomo': ['solver', 'solver_io', 'solver_options']
#         }
#         if keys[0] in values and values[keys[0]] == 'pyomo' and not _backend_options.keys

def calliope_version_validation(cls, _version, values):
    """Validator function for a range config object"""
    if _version != CALLIOPE_VERSION:
        raise ValueError(
            f"Calliope version mismatch: model specifies {_version} but running {CALLIOPE_VERSION}"
        )
    else:
        return _version


# def mask_validation(
#     key, keys, **opts
# ):

#     """
#     if function is 'extreme', 'tech' is allowed; if function is 'extreme_diff', 'tech0' and 'tech1' are allowed.
#     """


# def mask_options_var_validation():
#     """
#     string can only be one of the parameters given in 'constraints' for techs, and only if that parameter allows data to be loaded from file as timeseries (e.g. 'resource')
#     """


# def mask_options_tech_validation():
#     """
#     string can only be one of the user-defined techs
#     """


# def function_option_validation():
#    """
#    If model.time_aggregation.function is 'apply_clustering', only 'clustering_func', 'how', and 'k' can be defined. Only ff model.time_aggregation.clustering_func is 'kmeans' can 'k' be defined. If model.time_aggregation.function is 'resample', only 'resolution' can be defined.
#    """


# def timeseries_data_validation():
#     """
#     string:pandas.DataFrame pairs, where string must be one of the 'file=...' strings found in the data.
#     NOTE: we'll probably  get rid of this configuration as it is simply exposing implementation to the user
#     """


def timeseries_dateformat_validation(cls, _dateformat, values):
    """
    This string must be a valid datetime format string, e.g. '%Y-%m-%d %H:%M:%S'
    """
    try:
        parser.parse(datetime.now.strftime(_dateformat))
        return _dateformat
    except parser.ParserError:
        raise ValidationError("Unknown format codes used in timeseries date format")


# def validate_clustering_consistency():
    # # Don't allow time clustering with cyclic storage if not also using
    # # storage_inter_cluster
    # storage_inter_cluster = "model.time.function_options.storage_inter_cluster"
    # if (
    #     config_model.get_key("model.time.function", None) == "apply_clustering"
    #     and config_model.get_key("run.cyclic_storage", True)
    #     and not config_model.get_key(storage_inter_cluster, True)
    # ):
    #     errors.append(
    #         "When time clustering, cannot have cyclic storage constraints if "
    #         "`storage_inter_cluster` decision variable is not activated."
    #     )

    # ALSO:
    # Check for storage_inter_cluster not being used together with storage_discharge_depth

    # if hasattr(model_data, "clusters") and hasattr(
    #     model_data, "storage_discharge_depth"
    # ):
    #     errors.append(
    #         "storage_discharge_depth is currently not allowed when time clustering is active."
    #     )

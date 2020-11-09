
def allowed_in_validation(
    key: str, keys: Sequence[str], validator_params, **opts
) -> Dict[str, classmethod]:
    """
    Check if a setting is allowed for this tech group.
    """

    @validator(key, **opts)
    def _allowed_in_validation(cls, _setting: str, values):
        """Validator function for tech-group allowed settings."""
        if 
            raise ValueError(
                f"Calliope version mismatch: model specifies {_version} but running {CALLIOPE_VERSION}"
            )
        return _version

    return {"allowed_in_validation": _allowed_in_validation}


def cost_class_validation()
    """
    Look back at config and check that the cost classes defined in the objective 
    options match those defined as cost classes in the data.
    NOTE: this should cover all instances of CostClassDict!
    """

def node_coordinate_validation():
    """
    Can only define [x, y] or [lat, lon], no other combination of keys, e.g. [x, y, lat, lon], [x, lat]
    and all locations must be consistent, all [x, y] or all [lat, lon]
    """


def node_validation():
    """
    If 'techs' key defined, 'transmission_node' cannot be set to True. Although 
    'transmission_node' is somewhat exposing implementation to the user, and 
    could possibly be removed entirely
    """


def carrier_key_choice_validation():
    """
    NOTE: this is dealt with now by 'allowed_in'
    The allowed carrier keys that can be used depends on the top-level tech_group
    associated with each tech's parent.
    """


def carrier_validation(direction):
    """
    String must match one of the carriers defined under [{direction}, {direction}_2, {direction}_3]
    for this tech
    """

def no_carrier_may_be_called_resource():
    """
    `resource` is special, you can't call a carrier that.
    """

def error_if_a_technology_is_defined_twice_in_opposite_directions():
    """
    What the function name says.
    """


# def objective_options_validation(
#     key: str, keys: Sequence[str], **opts
# ) -> Dict[str, classmethod]:
#     @validator(key, **opts)
#     def _objective_options_validation(cls, _objective, values):
#         """
#         'cost_class' and 'sense' need to be defined if run.objective is 'minmax_cost_optimisation'
#         """
#         if _objective == 'minmax_cost_optimization':
#             if "cost_class" not in values or "sense" not in values:
#                 return ValueError("minmax_cost_optimisation chosen with either cost_class or sense undefined")
#         return _objective

#     return {"objective_options_validation", _objective_options_validation}

def export_cost_validation(
    key, keys, **opts
):
    @validator(key, **opts)
    def _export_cost_validation(cls, _export, values):
        """
        Can only define an export cost if an export carrier has been defined for the same technology
        """
        if 


def energy_cap_per_unit_requires_units_to_be_specified():

def storage_cap_per_unit_requires_units_to_be_specified():

def force_resource_requires_finite_resource():

def warn_if_group_constraint_contains_no_valid_loctechs():

def warn_if_loctech_is_defined_in_group_constraint_but_not_in_model():

def storage_initial_being_gte_to_storage_discharge_depth():


##
# Timeseries specific things follow below
##

def loc_tech_cannot_have_force_resource_and_infinite_resource():

def ensure_that_if_a_tech_has_negative_costs_there_is_a_max_cap_defined():
    caps = ["energy_cap", "storage_cap", "resource_cap", "resource_area"]
    costs = ["cost_" + i in model_data.data_vars.keys()]

def demand_only_allowed_negative_resource():

def supply_only_allowed_positive_resource():



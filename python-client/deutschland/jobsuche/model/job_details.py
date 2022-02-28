"""
    Arbeitsagentur Jobsuche API

    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br> Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:<br><br> **ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a <br> **ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8. **Achtung**: der OAuth header muss 'OAuthAccessToken' heißen.<br><br> Die API verfügt außerdem nicht über ein gültiges TLS Zertifikat. Deswegen sollte die TLS-Validierung deaktiviert werden.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.jobsuche.exceptions import ApiAttributeError
from deutschland.jobsuche.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    OpenApiModel,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


def lazy_import():
    from deutschland.jobsuche.model.job_details_arbeitgeber_adresse import (
        JobDetailsArbeitgeberAdresse,
    )
    from deutschland.jobsuche.model.job_details_arbeitsorte import JobDetailsArbeitsorte
    from deutschland.jobsuche.model.job_details_ausbildungen import (
        JobDetailsAusbildungen,
    )
    from deutschland.jobsuche.model.job_details_fertigkeiten import (
        JobDetailsFertigkeiten,
    )
    from deutschland.jobsuche.model.job_details_fuehrungskompetenzen import (
        JobDetailsFuehrungskompetenzen,
    )
    from deutschland.jobsuche.model.job_details_links import JobDetailsLinks
    from deutschland.jobsuche.model.job_details_mobilitaet import JobDetailsMobilitaet
    from deutschland.jobsuche.model.job_details_sprachkenntnisse import (
        JobDetailsSprachkenntnisse,
    )

    globals()["JobDetailsArbeitgeberAdresse"] = JobDetailsArbeitgeberAdresse
    globals()["JobDetailsArbeitsorte"] = JobDetailsArbeitsorte
    globals()["JobDetailsAusbildungen"] = JobDetailsAusbildungen
    globals()["JobDetailsFertigkeiten"] = JobDetailsFertigkeiten
    globals()["JobDetailsFuehrungskompetenzen"] = JobDetailsFuehrungskompetenzen
    globals()["JobDetailsLinks"] = JobDetailsLinks
    globals()["JobDetailsMobilitaet"] = JobDetailsMobilitaet
    globals()["JobDetailsSprachkenntnisse"] = JobDetailsSprachkenntnisse


class JobDetails(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "aktuelle_veroeffentlichungsdatum": (date,),  # noqa: E501
            "laufzeit_bis": (date,),  # noqa: E501
            "angebotsart": (str,),  # noqa: E501
            "arbeitgeber": (str,),  # noqa: E501
            "branchenbezeichnung": (str,),  # noqa: E501
            "arbeitgeber_hash_id": (str,),  # noqa: E501
            "arbeitsorte": ([JobDetailsArbeitsorte],),  # noqa: E501
            "arbeitszeitmodelle": ([str],),  # noqa: E501
            "befristung": (str,),  # noqa: E501
            "betriebsgroesse": (str,),  # noqa: E501
            "eintrittsdatum": (date,),  # noqa: E501
            "erste_veroeffentlichungsdatum": (date,),  # noqa: E501
            "freie_bezeichnung": (str,),  # noqa: E501
            "hash_id": (str,),  # noqa: E501
            "hauptberuf": (str,),  # noqa: E501
            "modifikations_timestamp": (str,),  # noqa: E501
            "stellenbeschreibung": (str,),  # noqa: E501
            "referenznummer": (str,),  # noqa: E501
            "fuer_fluechtlinge_geeignet": (bool,),  # noqa: E501
            "nur_fuer_schwerbehinderte": (bool,),  # noqa: E501
            "anzahl_offene_stellen": (int,),  # noqa: E501
            "arbeitgeber_adresse": (JobDetailsArbeitgeberAdresse,),  # noqa: E501
            "fertigkeiten": ([JobDetailsFertigkeiten],),  # noqa: E501
            "sprachkenntnisse": ([JobDetailsSprachkenntnisse],),  # noqa: E501
            "staerken": ([str],),  # noqa: E501
            "mobilitaet": (JobDetailsMobilitaet,),  # noqa: E501
            "berufserfahrung": (str,),  # noqa: E501
            "fuehrungskompetenzen": (JobDetailsFuehrungskompetenzen,),  # noqa: E501
            "ausbildungen": ([JobDetailsAusbildungen],),  # noqa: E501
            "arbeitgeberdarstellung_url": (str,),  # noqa: E501
            "haupt_dkz": (str,),  # noqa: E501
            "ist_betreut": (bool,),  # noqa: E501
            "ist_google_jobs_relevant": (bool,),  # noqa: E501
            "angebotsart_gruppe": (str,),  # noqa: E501
            "anzeige_anonym": (bool,),  # noqa: E501
            "links": (JobDetailsLinks,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "aktuelle_veroeffentlichungsdatum": "aktuelleVeroeffentlichungsdatum",  # noqa: E501
        "laufzeit_bis": "laufzeitBis",  # noqa: E501
        "angebotsart": "angebotsart",  # noqa: E501
        "arbeitgeber": "arbeitgeber",  # noqa: E501
        "branchenbezeichnung": "branchenbezeichnung",  # noqa: E501
        "arbeitgeber_hash_id": "arbeitgeberHashId",  # noqa: E501
        "arbeitsorte": "arbeitsorte",  # noqa: E501
        "arbeitszeitmodelle": "arbeitszeitmodelle",  # noqa: E501
        "befristung": "befristung",  # noqa: E501
        "betriebsgroesse": "betriebsgroesse",  # noqa: E501
        "eintrittsdatum": "eintrittsdatum",  # noqa: E501
        "erste_veroeffentlichungsdatum": "ersteVeroeffentlichungsdatum",  # noqa: E501
        "freie_bezeichnung": "freieBezeichnung",  # noqa: E501
        "hash_id": "hashId",  # noqa: E501
        "hauptberuf": "hauptberuf",  # noqa: E501
        "modifikations_timestamp": "modifikationsTimestamp",  # noqa: E501
        "stellenbeschreibung": "stellenbeschreibung",  # noqa: E501
        "referenznummer": "referenznummer",  # noqa: E501
        "fuer_fluechtlinge_geeignet": "fuerFluechtlingeGeeignet",  # noqa: E501
        "nur_fuer_schwerbehinderte": "nurFuerSchwerbehinderte",  # noqa: E501
        "anzahl_offene_stellen": "anzahlOffeneStellen",  # noqa: E501
        "arbeitgeber_adresse": "arbeitgeberAdresse",  # noqa: E501
        "fertigkeiten": "fertigkeiten",  # noqa: E501
        "sprachkenntnisse": "sprachkenntnisse",  # noqa: E501
        "staerken": "staerken",  # noqa: E501
        "mobilitaet": "mobilitaet",  # noqa: E501
        "berufserfahrung": "berufserfahrung",  # noqa: E501
        "fuehrungskompetenzen": "fuehrungskompetenzen",  # noqa: E501
        "ausbildungen": "ausbildungen",  # noqa: E501
        "arbeitgeberdarstellung_url": "arbeitgeberdarstellungUrl",  # noqa: E501
        "haupt_dkz": "hauptDkz",  # noqa: E501
        "ist_betreut": "istBetreut",  # noqa: E501
        "ist_google_jobs_relevant": "istGoogleJobsRelevant",  # noqa: E501
        "angebotsart_gruppe": "angebotsartGruppe",  # noqa: E501
        "anzeige_anonym": "anzeigeAnonym",  # noqa: E501
        "links": "_links",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """JobDetails - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            aktuelle_veroeffentlichungsdatum (date): [optional]  # noqa: E501
            laufzeit_bis (date): [optional]  # noqa: E501
            angebotsart (str): [optional]  # noqa: E501
            arbeitgeber (str): [optional]  # noqa: E501
            branchenbezeichnung (str): [optional]  # noqa: E501
            arbeitgeber_hash_id (str): [optional]  # noqa: E501
            arbeitsorte ([JobDetailsArbeitsorte]): [optional]  # noqa: E501
            arbeitszeitmodelle ([str]): [optional]  # noqa: E501
            befristung (str): [optional]  # noqa: E501
            betriebsgroesse (str): [optional]  # noqa: E501
            eintrittsdatum (date): [optional]  # noqa: E501
            erste_veroeffentlichungsdatum (date): [optional]  # noqa: E501
            freie_bezeichnung (str): [optional]  # noqa: E501
            hash_id (str): [optional]  # noqa: E501
            hauptberuf (str): [optional]  # noqa: E501
            modifikations_timestamp (str): [optional]  # noqa: E501
            stellenbeschreibung (str): [optional]  # noqa: E501
            referenznummer (str): [optional]  # noqa: E501
            fuer_fluechtlinge_geeignet (bool): [optional]  # noqa: E501
            nur_fuer_schwerbehinderte (bool): [optional]  # noqa: E501
            anzahl_offene_stellen (int): [optional]  # noqa: E501
            arbeitgeber_adresse (JobDetailsArbeitgeberAdresse): [optional]  # noqa: E501
            fertigkeiten ([JobDetailsFertigkeiten]): [optional]  # noqa: E501
            sprachkenntnisse ([JobDetailsSprachkenntnisse]): [optional]  # noqa: E501
            staerken ([str]): [optional]  # noqa: E501
            mobilitaet (JobDetailsMobilitaet): [optional]  # noqa: E501
            berufserfahrung (str): [optional]  # noqa: E501
            fuehrungskompetenzen (JobDetailsFuehrungskompetenzen): [optional]  # noqa: E501
            ausbildungen ([JobDetailsAusbildungen]): [optional]  # noqa: E501
            arbeitgeberdarstellung_url (str): [optional]  # noqa: E501
            haupt_dkz (str): [optional]  # noqa: E501
            ist_betreut (bool): [optional]  # noqa: E501
            ist_google_jobs_relevant (bool): [optional]  # noqa: E501
            angebotsart_gruppe (str): [optional]  # noqa: E501
            anzeige_anonym (bool): [optional]  # noqa: E501
            links (JobDetailsLinks): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """JobDetails - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            aktuelle_veroeffentlichungsdatum (date): [optional]  # noqa: E501
            laufzeit_bis (date): [optional]  # noqa: E501
            angebotsart (str): [optional]  # noqa: E501
            arbeitgeber (str): [optional]  # noqa: E501
            branchenbezeichnung (str): [optional]  # noqa: E501
            arbeitgeber_hash_id (str): [optional]  # noqa: E501
            arbeitsorte ([JobDetailsArbeitsorte]): [optional]  # noqa: E501
            arbeitszeitmodelle ([str]): [optional]  # noqa: E501
            befristung (str): [optional]  # noqa: E501
            betriebsgroesse (str): [optional]  # noqa: E501
            eintrittsdatum (date): [optional]  # noqa: E501
            erste_veroeffentlichungsdatum (date): [optional]  # noqa: E501
            freie_bezeichnung (str): [optional]  # noqa: E501
            hash_id (str): [optional]  # noqa: E501
            hauptberuf (str): [optional]  # noqa: E501
            modifikations_timestamp (str): [optional]  # noqa: E501
            stellenbeschreibung (str): [optional]  # noqa: E501
            referenznummer (str): [optional]  # noqa: E501
            fuer_fluechtlinge_geeignet (bool): [optional]  # noqa: E501
            nur_fuer_schwerbehinderte (bool): [optional]  # noqa: E501
            anzahl_offene_stellen (int): [optional]  # noqa: E501
            arbeitgeber_adresse (JobDetailsArbeitgeberAdresse): [optional]  # noqa: E501
            fertigkeiten ([JobDetailsFertigkeiten]): [optional]  # noqa: E501
            sprachkenntnisse ([JobDetailsSprachkenntnisse]): [optional]  # noqa: E501
            staerken ([str]): [optional]  # noqa: E501
            mobilitaet (JobDetailsMobilitaet): [optional]  # noqa: E501
            berufserfahrung (str): [optional]  # noqa: E501
            fuehrungskompetenzen (JobDetailsFuehrungskompetenzen): [optional]  # noqa: E501
            ausbildungen ([JobDetailsAusbildungen]): [optional]  # noqa: E501
            arbeitgeberdarstellung_url (str): [optional]  # noqa: E501
            haupt_dkz (str): [optional]  # noqa: E501
            ist_betreut (bool): [optional]  # noqa: E501
            ist_google_jobs_relevant (bool): [optional]  # noqa: E501
            angebotsart_gruppe (str): [optional]  # noqa: E501
            anzeige_anonym (bool): [optional]  # noqa: E501
            links (JobDetailsLinks): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.8.4, generator: @autorest/python@6.0.1)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import DigitalOceanClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    AccountOperations,
    ActionsOperations,
    AppsOperations,
    BalanceOperations,
    BillingHistoryOperations,
    CdnOperations,
    CertificatesOperations,
    DatabasesOperations,
    DomainsOperations,
    DropletActionsOperations,
    DropletsOperations,
    FirewallsOperations,
    FloatingIPsActionOperations,
    FloatingIPsOperations,
    ImageActionsOperations,
    ImagesOperations,
    InvoicesOperations,
    KubernetesOperations,
    LoadBalancersOperations,
    MonitoringOperations,
    OneClicksOperations,
    ProjectsOperations,
    RegionsOperations,
    RegistryOperations,
    ReservedIPsActionsOperations,
    ReservedIPsOperations,
    SizesOperations,
    SnapshotsOperations,
    SshKeysOperations,
    TagsOperations,
    VolumeActionsOperations,
    VolumeSnapshotsOperations,
    VolumesOperations,
    VpcsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

    from azure.core.credentials import TokenCredential


class DigitalOceanClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Introduction
    ============

    The DigitalOcean API allows you to manage Droplets and resources within the
    DigitalOcean cloud in a simple, programmatic way using conventional HTTP requests.

    All of the functionality that you are familiar with in the DigitalOcean
    control panel is also available through the API, allowing you to script the
    complex actions that your situation requires.

    The API documentation will start with a general overview about the design
    and technology that has been implemented, followed by reference information
    about specific endpoints.

    Requests
    --------

    Any tool that is fluent in HTTP can communicate with the API simply by
    requesting the correct URI. Requests should be made using the HTTPS protocol
    so that traffic is encrypted. The interface responds to different methods
    depending on the action required.

    .. list-table::
       :header-rows: 1

       * - Method
         - Usage
       * - GET
         - For simple retrieval of information about your account, Droplets, or environment, you
    should use the GET method.  The information you request will be returned to you as a JSON
    object. The attributes defined by the JSON object can be used to form additional requests.  Any
    request using the GET method is read-only and will not affect any of the objects you are
    querying.
       * - DELETE
         - To destroy a resource and remove it from your account and environment, the DELETE method
    should be used.  This will remove the specified object if it is found.  If it is not found, the
    operation will return a response indicating that the object was not found. This idempotency
    means that you do not have to check for a resource's availability prior to issuing a delete
    command, the final state will be the same regardless of its existence.
       * - PUT
         - To update the information about a resource in your account, the PUT method is available.
    Like the DELETE Method, the PUT method is idempotent.  It sets the state of the target using
    the provided values, regardless of their current values. Requests using the PUT method do not
    need to check the current attributes of the object.
       * - PATCH
         - Some resources support partial modification. In these cases, the PATCH method is
    available. Unlike PUT which generally requires a complete representation of a resource, a PATCH
    request is is a set of instructions on how to modify a resource updating only specific
    attributes.
       * - POST
         - To create a new object, your request should specify the POST method. The POST request
    includes all of the attributes necessary to create a new object.  When you wish to create a new
    object, send a POST request to the target endpoint.
       * - HEAD
         - Finally, to retrieve metadata information, you should use the HEAD method to get the
    headers.  This returns only the header of what would be returned with an associated GET
    request. Response headers contain some useful information about your API access and the results
    that are available for your request. For instance, the headers contain your current rate-limit
    value and the amount of time available until the limit resets. It also contains metrics about
    the total number of objects found, pagination information, and the total content length.


    HTTP Statuses
    -------------

    Along with the HTTP methods that the API responds to, it will also return
    standard HTTP statuses, including error codes.

    In the event of a problem, the status will contain the error code, while the
    body of the response will usually contain additional information about the
    problem that was encountered.

    In general, if the status returned is in the 200 range, it indicates that
    the request was fulfilled successfully and that no error was encountered.

    Return codes in the 400 range typically indicate that there was an issue
    with the request that was sent. Among other things, this could mean that you
    did not authenticate correctly, that you are requesting an action that you
    do not have authorization for, that the object you are requesting does not
    exist, or that your request is malformed.

    If you receive a status in the 500 range, this generally indicates a
    server-side problem. This means that we are having an issue on our end and
    cannot fulfill your request currently.

    400 and 500 level error responses will include a JSON object in their body,
    including the following attributes:

    .. list-table::
       :header-rows: 1

       * - Name
         - Type
         - Description
       * - id
         - string
         - A short identifier corresponding to the HTTP status code returned. For example, the ID
    for a response returning a 404 status code would be "not_found."
       * - message
         - string
         - A message providing additional information about the error, including details to help
    resolve it when possible.
       * - request_id
         - string
         - Optionally, some endpoints may include a request ID that should be provided when
    reporting bugs or opening support tickets to help identify the issue.


    Example Error Response
    ^^^^^^^^^^^^^^^^^^^^^^

    .. code-block::

           HTTP/1.1 403 Forbidden
           {
             "id":       "forbidden",
             "message":  "You do not have access for the attempted action."
           }

    Responses
    ---------

    When a request is successful, a response body will typically be sent back in
    the form of a JSON object. An exception to this is when a DELETE request is
    processed, which will result in a successful HTTP 204 status and an empty
    response body.

    Inside of this JSON object, the resource root that was the target of the
    request will be set as the key. This will be the singular form of the word
    if the request operated on a single object, and the plural form of the word
    if a collection was processed.

    For example, if you send a GET request to ``/v2/droplets/$DROPLET_ID`` you
    will get back an object with a key called "\ ``droplet``\ ". However, if you send
    the GET request to the general collection at ``/v2/droplets``\ , you will get
    back an object with a key called "\ ``droplets``\ ".

    The value of these keys will generally be a JSON object for a request on a
    single object and an array of objects for a request on a collection of
    objects.

    Response for a Single Object
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block::

           {
               "droplet": {
                   "name": "example.com"
                   . . .
               }
           }

    Response for an Object Collection
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block::

           {
               "droplets": [
                   {
                       "name": "example.com"
                       . . .
                   },
                   {
                       "name": "second.com"
                       . . .
                   }
               ]
           }

    Meta
    ----

    In addition to the main resource root, the response may also contain a
    ``meta`` object. This object contains information about the response itself.

    The ``meta`` object contains a ``total`` key that is set to the total number of
    objects returned by the request. This has implications on the ``links`` object
    and pagination.

    The ``meta`` object will only be displayed when it has a value. Currently, the
    ``meta`` object will have a value when a request is made on a collection (like
    ``droplets`` or ``domains``\ ).

    Sample Meta Object
    ^^^^^^^^^^^^^^^^^^

    .. code-block::

           {
               . . .
               "meta": {
                   "total": 43
               }
               . . .
           }

    Links & Pagination
    ------------------

    The ``links`` object is returned as part of the response body when pagination
    is enabled. By default, 20 objects are returned per page. If the response
    contains 20 objects or fewer, no ``links`` object will be returned. If the
    response contains more than 20 objects, the first 20 will be returned along
    with the ``links`` object.

    You can request a different pagination limit or force pagination by
    appending ``?per_page=`` to the request with the number of items you would
    like per page. For instance, to show only two results per page, you could
    add ``?per_page=2`` to the end of your query. The maximum number of results
    per page is 200.

    The ``links`` object contains a ``pages`` object. The ``pages`` object, in turn,
    contains keys indicating the relationship of additional pages. The values of
    these are the URLs of the associated pages. The keys will be one of the
    following:


    * **first**\ : The URI of the first page of results.
    * **prev**\ : The URI of the previous sequential page of results.
    * **next**\ : The URI of the next sequential page of results.
    * **last**\ : The URI of the last page of results.

    The ``pages`` object will only include the links that make sense. So for the
    first page of results, no ``first`` or ``prev`` links will ever be set. This
    convention holds true in other situations where a link would not make sense.

    Sample Links Object
    ^^^^^^^^^^^^^^^^^^^

    .. code-block::

           {
               . . .
               "links": {
                   "pages": {
                       "last": "https://api.digitalocean.com/v2/images?page=2",
                       "next": "https://api.digitalocean.com/v2/images?page=2"
                   }
               }
               . . .
           }

    Rate Limit
    ----------

    Requests through the API are rate limited per OAuth token. Current rate limits:


    * 5,000 requests per hour
    * 250 requests per minute (5% of the hourly total)

    Once you exceed either limit, you will be rate limited until the next cycle
    starts. Space out any requests that you would otherwise issue in bursts for
    the best results.

    The rate limiting information is contained within the response headers of
    each request. The relevant headers are:


    * **RateLimit-Limit**\ : The number of requests that can be made per hour.
    * **RateLimit-Remaining**\ : The number of requests that remain before you hit your request
    limit. See the information below for how the request limits expire.
    * **RateLimit-Reset**\ : This represents the time when the oldest request will expire. The
    value is given in `Unix epoch time <http://en.wikipedia.org/wiki/Unix_time>`_. See below for
    more information about how request limits expire.

    As long as the ``RateLimit-Remaining`` count is above zero, you will be able
    to make additional requests.

    The way that a request expires and is removed from the current limit count
    is important to understand. Rather than counting all of the requests for an
    hour and resetting the ``RateLimit-Remaining`` value at the end of the hour,
    each request instead has its own timer.

    This means that each request contributes toward the ``RateLimit-Remaining``
    count for one complete hour after the request is made. When that request's
    timer runs out, it is no longer counted towards the request limit.

    This has implications on the meaning of the ``RateLimit-Reset`` header as
    well. Because the entire rate limit is not reset at one time, the value of
    this header is set to the time when the *oldest* request will expire.

    Keep this in mind if you see your ``RateLimit-Reset`` value change, but not
    move an entire hour into the future.

    If the ``RateLimit-Remaining`` reaches zero, subsequent requests will receive
    a 429 error code until the request reset has been reached. You can see the
    format of the response in the examples.

    **Note:** The following endpoints have special rate limit requirements that
    are independent of the limits defined above.


    * Only 12 ``POST`` requests to the ``/v2/floating_ips`` endpoint to create Floating IPs can be
    made per 60 seconds.
    * Only 10 ``GET`` requests to the ``/v2/account/keys`` endpoint to list SSH keys can be made
    per 60 seconds.

    Sample Rate Limit Headers
    ^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block::

           . . .
           RateLimit-Limit: 1200
           RateLimit-Remaining: 1193
           RateLimit-Reset: 1402425459
           . . .

    Sample Rate Exceeded Response
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block::

           429 Too Many Requests
           {
                   id: "too_many_requests",
                   message: "API Rate limit exceeded."
           }

    Curl Examples
    -------------

    Throughout this document, some example API requests will be given using the
    ``curl`` command. This will allow us to demonstrate the various endpoints in a
    simple, textual format.

      These examples assume that you are using a Linux or macOS command line. To run
    these commands on a Windows machine, you can either use cmd.exe, PowerShell, or WSL:


    *
      For cmd.exe, use the ``set VAR=VALUE`` `syntax
    <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/set_1>`_
      to define environment variables, call them with ``%VAR%``\ , then replace all backslashes (\
    ``\``\ ) in the examples with carets (\ ``^``\ ).

    *
      For PowerShell, use the ``$Env:VAR = "VALUE"`` `syntax
    <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.2>`_
      to define environment variables, call them with ``$Env:VAR``\ , then replace ``curl`` with
    ``curl.exe`` and all backslashes (\ ``\``\ ) in the examples with backticks (\ ``` ``\ ).

    *
      WSL is a compatibility layer that allows you to emulate a Linux terminal on a Windows
    machine.
      Install WSL with our `community tutorial
    <https://www.digitalocean.com/community/tutorials/how-to-install-the-windows-subsystem-for-linux-2-on-microsoft-windows-10>`_\
    ,
      then follow this API documentation normally.

    The names of account-specific references (like Droplet IDs, for instance)
    will be represented by variables. For instance, a Droplet ID may be
    represented by a variable called ``$DROPLET_ID``. You can set the associated
    variables in your environment if you wish to use the examples without
    modification.

    The first variable that you should set to get started is your OAuth
    authorization token. The next section will go over the details of this, but
    you can set an environmental variable for it now.

    Generate a token by going to the `Apps & API
    <https://cloud.digitalocean.com/settings/applications>`_
    section of the DigitalOcean control panel. Use an existing token if you have
    saved one, or generate a new token with the "Generate new token" button.
    Copy the generated token and use it to set and export the TOKEN variable in
    your environment as the example shows.

    You may also wish to set some other variables now or as you go along. For
    example, you may wish to set the ``DROPLET_ID`` variable to one of your
    Droplet IDs since this will be used frequently in the API.

    If you are following along, make sure you use a Droplet ID that you control
    so that your commands will execute correctly.

    If you need access to the headers of a response through ``curl``\ , you can pass
    the ``-i`` flag to display the header information along with the body. If you
    are only interested in the header, you can instead pass the ``-I`` flag, which
    will exclude the response body entirely.

    Set and Export your OAuth Token
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block::

       export DIGITALOCEAN_TOKEN=your_token_here

    Set and Export a Variable
    ^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block::

       export DROPLET_ID=1111111

    Parameters
    ----------

    There are two different ways to pass parameters in a request with the API.

    When passing parameters to create or update an object, parameters should be
    passed as a JSON object containing the appropriate attribute names and
    values as key-value pairs. When you use this format, you should specify that
    you are sending a JSON object in the header. This is done by setting the
    ``Content-Type`` header to ``application/json``. This ensures that your request
    is interpreted correctly.

    When passing parameters to filter a response on GET requests, parameters can
    be passed using standard query attributes. In this case, the parameters
    would be embedded into the URI itself by appending a ``?`` to the end of the
    URI and then setting each attribute with an equal sign. Attributes can be
    separated with a ``&``. Tools like ``curl`` can create the appropriate URI when
    given parameters and values; this can also be done using the ``-F`` flag and
    then passing the key and value as an argument. The argument should take the
    form of a quoted string with the attribute being set to a value with an
    equal sign.

    Pass Parameters as a JSON Object
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block::

           curl -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
               -H "Content-Type: application/json" \
               -d '{"name": "example.com", "ip_address": "127.0.0.1"}' \
               -X POST "https://api.digitalocean.com/v2/domains"

    Pass Filter Parameters as a Query String
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. code-block::

            curl -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
                -X GET \
                "https://api.digitalocean.com/v2/images?private=true"

    Cross Origin Resource Sharing
    -----------------------------

    In order to make requests to the API from other domains, the API implements
    Cross Origin Resource Sharing (CORS) support.

    CORS support is generally used to create AJAX requests outside of the domain
    that the request originated from. This is necessary to implement projects
    like control panels utilizing the API. This tells the browser that it can
    send requests to an outside domain.

    The procedure that the browser initiates in order to perform these actions
    (other than GET requests) begins by sending a "preflight" request. This sets
    the ``Origin`` header and uses the ``OPTIONS`` method. The server will reply
    back with the methods it allows and some of the limits it imposes. The
    client then sends the actual request if it falls within the allowed
    constraints.

    This process is usually done in the background by the browser, but you can
    use curl to emulate this process using the example provided. The headers
    that will be set to show the constraints are:


    * **Access-Control-Allow-Origin**\ : This is the domain that is sent by the client or browser
    as the origin of the request. It is set through an ``Origin`` header.
    * **Access-Control-Allow-Methods**\ : This specifies the allowed options for requests from that
    domain. This will generally be all available methods.
    * **Access-Control-Expose-Headers**\ : This will contain the headers that will be available to
    requests from the origin domain.
    * **Access-Control-Max-Age**\ : This is the length of time that the access is considered valid.
    After this expires, a new preflight should be sent.
    * **Access-Control-Allow-Credentials**\ : This will be set to ``true``. It basically allows you
    to send your OAuth token for authentication.

    You should not need to be concerned with the details of these headers,
    because the browser will typically do all of the work for you.

    :ivar one_clicks: OneClicksOperations operations
    :vartype one_clicks: digitalocean.operations.OneClicksOperations
    :ivar account: AccountOperations operations
    :vartype account: digitalocean.operations.AccountOperations
    :ivar ssh_keys: SshKeysOperations operations
    :vartype ssh_keys: digitalocean.operations.SshKeysOperations
    :ivar actions: ActionsOperations operations
    :vartype actions: digitalocean.operations.ActionsOperations
    :ivar apps: AppsOperations operations
    :vartype apps: digitalocean.operations.AppsOperations
    :ivar cdn: CdnOperations operations
    :vartype cdn: digitalocean.operations.CdnOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates: digitalocean.operations.CertificatesOperations
    :ivar balance: BalanceOperations operations
    :vartype balance: digitalocean.operations.BalanceOperations
    :ivar billing_history: BillingHistoryOperations operations
    :vartype billing_history: digitalocean.operations.BillingHistoryOperations
    :ivar invoices: InvoicesOperations operations
    :vartype invoices: digitalocean.operations.InvoicesOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: digitalocean.operations.DatabasesOperations
    :ivar domains: DomainsOperations operations
    :vartype domains: digitalocean.operations.DomainsOperations
    :ivar droplets: DropletsOperations operations
    :vartype droplets: digitalocean.operations.DropletsOperations
    :ivar droplet_actions: DropletActionsOperations operations
    :vartype droplet_actions: digitalocean.operations.DropletActionsOperations
    :ivar firewalls: FirewallsOperations operations
    :vartype firewalls: digitalocean.operations.FirewallsOperations
    :ivar floating_ips: FloatingIPsOperations operations
    :vartype floating_ips: digitalocean.operations.FloatingIPsOperations
    :ivar floating_ips_action: FloatingIPsActionOperations operations
    :vartype floating_ips_action: digitalocean.operations.FloatingIPsActionOperations
    :ivar images: ImagesOperations operations
    :vartype images: digitalocean.operations.ImagesOperations
    :ivar image_actions: ImageActionsOperations operations
    :vartype image_actions: digitalocean.operations.ImageActionsOperations
    :ivar kubernetes: KubernetesOperations operations
    :vartype kubernetes: digitalocean.operations.KubernetesOperations
    :ivar load_balancers: LoadBalancersOperations operations
    :vartype load_balancers: digitalocean.operations.LoadBalancersOperations
    :ivar monitoring: MonitoringOperations operations
    :vartype monitoring: digitalocean.operations.MonitoringOperations
    :ivar projects: ProjectsOperations operations
    :vartype projects: digitalocean.operations.ProjectsOperations
    :ivar regions: RegionsOperations operations
    :vartype regions: digitalocean.operations.RegionsOperations
    :ivar registry: RegistryOperations operations
    :vartype registry: digitalocean.operations.RegistryOperations
    :ivar reserved_ips: ReservedIPsOperations operations
    :vartype reserved_ips: digitalocean.operations.ReservedIPsOperations
    :ivar reserved_ips_actions: ReservedIPsActionsOperations operations
    :vartype reserved_ips_actions: digitalocean.operations.ReservedIPsActionsOperations
    :ivar sizes: SizesOperations operations
    :vartype sizes: digitalocean.operations.SizesOperations
    :ivar snapshots: SnapshotsOperations operations
    :vartype snapshots: digitalocean.operations.SnapshotsOperations
    :ivar tags: TagsOperations operations
    :vartype tags: digitalocean.operations.TagsOperations
    :ivar volumes: VolumesOperations operations
    :vartype volumes: digitalocean.operations.VolumesOperations
    :ivar volume_actions: VolumeActionsOperations operations
    :vartype volume_actions: digitalocean.operations.VolumeActionsOperations
    :ivar volume_snapshots: VolumeSnapshotsOperations operations
    :vartype volume_snapshots: digitalocean.operations.VolumeSnapshotsOperations
    :ivar vpcs: VpcsOperations operations
    :vartype vpcs: digitalocean.operations.VpcsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :keyword endpoint: Service URL. Default value is "https://api.digitalocean.com".
    :paramtype endpoint: str
    """

    def __init__(
        self, credential: "TokenCredential", *, endpoint: str = "https://api.digitalocean.com", **kwargs: Any
    ) -> None:
        self._config = DigitalOceanClientConfiguration(credential=credential, **kwargs)
        self._client = PipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.one_clicks = OneClicksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.account = AccountOperations(self._client, self._config, self._serialize, self._deserialize)
        self.ssh_keys = SshKeysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.actions = ActionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.apps = AppsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.cdn = CdnOperations(self._client, self._config, self._serialize, self._deserialize)
        self.certificates = CertificatesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.balance = BalanceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.billing_history = BillingHistoryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.invoices = InvoicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.domains = DomainsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.droplets = DropletsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.droplet_actions = DropletActionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.firewalls = FirewallsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.floating_ips = FloatingIPsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.floating_ips_action = FloatingIPsActionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.images = ImagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.image_actions = ImageActionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.kubernetes = KubernetesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.load_balancers = LoadBalancersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.monitoring = MonitoringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.projects = ProjectsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.regions = RegionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registry = RegistryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.reserved_ips = ReservedIPsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.reserved_ips_actions = ReservedIPsActionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sizes = SizesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.snapshots = SnapshotsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.tags = TagsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.volumes = VolumesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.volume_actions = VolumeActionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.volume_snapshots = VolumeSnapshotsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.vpcs = VpcsOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DigitalOceanClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)

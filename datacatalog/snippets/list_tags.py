def list_tags(override_values):

    from google.api_core import retry

    # Overwite the following default values
    # to your own desired retry values.
    _DEFAULT_INITIAL_DELAY = 1.0  # unit in seconds
    _DEFAULT_MAXIMUM_DELAY = 60.0  # unit in seconds
    _DEFAULT_DELAY_MULTIPLIER = 2.0
    _DEFAULT_DEADLINE = 60.0 * 2.0  # unit in seconds

    my_retry = retry.Retry(
        initial=_DEFAULT_INITIAL_DELAY,
        maximum=_DEFAULT_MAXIMUM_DELAY,
        multiplier=_DEFAULT_DELAY_MULTIPLIER,
        deadline=_DEFAULT_DEADLINE,
    )
   
    # Google Cloud Platform project.
    project_id = "my-project"
    # Entry Group
    entry_group_id = "my_new_entry_group_id"
    # Entry
    entry_id = "my_new_entry_id"
    # Currently, Data Catalog stores metadata in the us-central1 region.
    location = "us-central1"

    # To facilitate testing, we replace values with alternatives
    # provided by the testing harness.
    project_id = override_values.get("project_id", project_id)
    entry_id = override_values.get("entry_id", entry_id)
    entry_group_id = override_values.get("entry_group_id", entry_group_id)

    # [START data_catalog_list_tags]
    datacatalog_client = datacatalog_v1.DataCatalogClient()


    request = datacatalog_v1.ListTagsRequest(dict(
        parent="projects/"+project_id+"/locations/"+location+"/entryGroups/"+entry_group_id+"/entries/"+entry_id,
        # Explicitly set pageSize to the max value 1K to
        # avoid making multiple API calls when        
        # entries have more than 10 tags.
        page_size=1000,
    ))

    # Set the retry= param to your own my_retry settings object
    tags = datacatalog_client.list_tags(request=request, retry=my_retry)

    # Print tags
    for tag in tags:
        print("Tag name: "+tag.name)
    
    # [END data_catalog_list_tags]

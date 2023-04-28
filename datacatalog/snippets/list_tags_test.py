import re
import list_tags

PROJECT_ID = ""
ENTRY = ""
ENTRY_GROUP = ""
def test_list_tags(capsys):
    override_values = {
        "project_id": PROJECT_ID,
        "entry_id": ENTRY,
        "entry_group_id": ENTRY_GROUP,
    }
    list_tags.list_tags(override_values)
    out, err = capsys.readouterr()
    assert re.search(
        f"(Retrieved entry .+ for BigQuery Dataset resource {dataset_resource})", out
    )

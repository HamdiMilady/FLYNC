from pathlib import Path

from flync.sdk.workspace.flync_workspace import FLYNCWorkspace

current_dir = Path(__file__).resolve().parent


def test_load_workspace_from_flync_object(get_flync_example_path):
    workspace_name_object = "flync_workspace_from_folder"
    loaded_ws = FLYNCWorkspace.load_workspace(
        workspace_name_object, get_flync_example_path
    )
    assert loaded_ws is not None
    # To be improved.
    assert loaded_ws.flync_model is not None
    assert loaded_ws.flync_model.ecus
    assert loaded_ws.flync_model.topology
    assert loaded_ws.flync_model.topology.system_topology
    assert loaded_ws.flync_model.general
    assert loaded_ws.flync_model.general.someip_config
    assert loaded_ws.flync_model.general.tcp_profiles
    assert loaded_ws.flync_model.metadata
    assert model_has_socket(loaded_ws)


def model_has_socket(loaded_ws: FLYNCWorkspace):
    for ecu in loaded_ws.flync_model.ecus:
        for controller in ecu.controllers:
            for interface in controller.interfaces:
                for vlan in interface.virtual_interfaces:
                    for address in vlan.addresses:
                        if address.sockets:
                            return True

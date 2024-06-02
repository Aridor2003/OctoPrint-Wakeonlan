# coding=utf-8

import octoprint.plugin
import socket
import struct
import flask

class WakeonlanPlugin(octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.SimpleApiPlugin
):

    def on_after_startup(self):
        self._logger.info("WakeOnLanPlugin has started")

    def get_settings_defaults(self):
        return dict(mac_address="00:00:00:00:00:00")

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False),
            dict(type="navbar", custom_bindings=True)
        ]

    def get_assets(self):
        return dict(
            js=["js/wol.js"],
            css=["css/wol.css"]
        )

    def send_wol_packet(self, mac):
        self._logger.info(f"Sending WOL packet to {mac}")
        addr_byte = mac.split(':')
        hw_addr = struct.pack('!6B', *[int(x, 16) for x in addr_byte])
        msg = b'\xff' * 6 + hw_addr * 16
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(msg, ('<broadcast>', 9))
        s.close()
        self._logger.info(f"Sent WOL packet to {mac}")

    def get_api_commands(self):
        return {"wake": []}

    def on_api_command(self, command, data):
        if command == "wake":
            mac_address = self._settings.get(["mac_address"])
            self._logger.info(f"Received WOL request for {mac_address}")
            self.send_wol_packet(mac_address)
            return flask.jsonify({"result": "success"})

    ##~~ Softwareupdate hook

    def get_update_information(self):
        return {
            "wakeonlan": {
                "displayName": "Wakeonlan Plugin",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "Aridor2003",
                "repo": "OctoPrint-Wakeonlan",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/Aridor2003/OctoPrint-Wakeonlan/archive/{target_version}.zip",
            }
        }


__plugin_name__ = "Wakeonlan Plugin"
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = WakeonlanPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }

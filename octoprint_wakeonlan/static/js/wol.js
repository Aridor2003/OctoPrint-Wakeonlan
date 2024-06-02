/*
 * View model for OctoPrint-Wakeonlan
 *
 * Author: Aridor
 * License: AGPLv3
 */
$(function() {
    function WakeonlanViewModel(parameters) {
        var self = this;
        self.settingsViewModel = parameters[0];

        self.wake = function() {
            OctoPrint.simpleApiCommand("wakeonlan", "wake", {});
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: WakeonlanViewModel,
        dependencies: [ "settingsViewModel" ],
        elements: [ "#navbar_plugin_wakeonlan" ]
    });
});

/* This software is licensed under a BSD license; see the LICENSE file for details. */

define_ibex_controller({
name: "SeparatorTer",

jqueryWidget: {
    _init: function () {
        this.cssPrefix = this.options._cssPrefix;
        this.utils = this.options._utils;
        this.finishedCallback = this.options._finishedCallback;

        this.ignoreFailure = dget(this.options, "ignoreFailure", false);
        this.style = this.ignoreFailure ? "normal" : (this.utils.getValueFromPreviousElement("failed") ? "error" : "normal");
        var x = this.utils.getValueFromPreviousElement("style");
        if (x) this.style = x;
        assert(this.style == "normal" || this.style == "error", "'style' property of Separator must either be 'normal' or 'error'");

        this.transfer_normal = dget(this.options, "normalTransfer", "keypress");
        assert(this.transfer_normal == "keypress" || typeof(this.transfer_normal) == "number",
               "Value of 'normalTransfer' option of Separator must either be the string 'keypress' or a number");

        this.transfer_error = dget(this.options, "errorTransfer", "keypress");
        assert(this.transfer_error == "keypress" || typeof(this.transfer_error) == "number",
               "Value of 'errorTransfer' option of Separator must either be the string 'keypress' or a number");

        var normal_message = dget(this.options, "normalMessage", "Press any key to continue.");
        var x = this.utils.getValueFromPreviousElement("normalMessage");
        if (x) normal_message = x;

        var error_message = dget(this.options, "errorMessage", "Wrong. Press any key to continue.");
        var x = this.utils.getValueFromPreviousElement("errorMessage");
        if (x) error_message = x;

        var p = $(document.createElement("p"));
        this.element.append(p);
        if     (this.style == "error") {
                this.element.addClass(this.cssPrefix + "next-item-failure-message");
                p.html(error_message);

        if (this.transfer_error == "keypress") {
            var t = this;
            this.safeBind($(document), 'keydown', function () {
            t.finishedCallback(null);
            return false;
            });
               }
            else {
                var t = this;
                    this.utils.setTimeout(function () {
                    t.finishedCallback(null);
                    }, this.transfer_error);
            }        
    }

        else {
            this.element.addClass(this.cssPrefix + "next-item-message");
            p.html(normal_message);

            if (this.transfer_normal == "keypress") {
            var t = this;
            this.safeBind($(document), 'keydown', function () {
            t.finishedCallback(null);
            return false;
            });
            }
            else {
                var t = this;
                this.utils.setTimeout(function () {
                    t.finishedCallback(null);
                }, this.transfer_normal);
            }
        }

    }
},

properties: {
    countsForProgressBar: false,
    htmlDescription: function (opts) {
        return $(document.createElement("div")).text(opts.normalMessage)[0];
    }
}
});
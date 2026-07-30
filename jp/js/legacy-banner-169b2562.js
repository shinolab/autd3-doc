(function () {
    "use strict";

    var SDK_REPO = "https://github.com/shinolab/autd3-sdk";
    var SDK_DOC_JA = "https://shinolab.github.io/autd3-sdk/";
    var SDK_DOC_EN = "https://shinolab.github.io/autd3-sdk/en/";

    function isJapanese() {
        return window.location.pathname.indexOf("/jp/") !== -1;
    }

    function build() {
        var ja = isJapanese();
        var doc = ja ? SDK_DOC_JA : SDK_DOC_EN;

        var banner = document.createElement("aside");
        banner.className = "legacy-banner";

        var icon = document.createElement("div");
        icon.className = "legacy-banner__icon";
        icon.textContent = "⚠️";

        var body = document.createElement("div");
        body.className = "legacy-banner__body";

        var head = document.createElement("p");
        var tail = document.createElement("p");

        if (ja) {
            head.innerHTML =
                "<strong>これは旧 AUTD3 シリーズのドキュメントである.</strong>";
            tail.innerHTML =
                '新規の開発は <a href="' + SDK_REPO + '">autd3-sdk</a> へ移行した. ' +
                'autd3-sdk は本シリーズとは<strong>非互換</strong>の新世代バージョンであり, ' +
                '新しく始める場合は <a href="' + doc + '">autd3-sdk のドキュメント</a> を参照すること.';
        } else {
            head.innerHTML =
                "<strong>This is the documentation for the legacy AUTD3 series.</strong>";
            tail.innerHTML =
                'New development has moved to <a href="' + SDK_REPO + '">autd3-sdk</a>, ' +
                'a new generation of the SDK that is <strong>not compatible</strong> with this series. ' +
                'If you are starting out, see the <a href="' + doc + '">autd3-sdk documentation</a> instead.';
        }

        body.appendChild(head);
        body.appendChild(tail);
        banner.appendChild(icon);
        banner.appendChild(body);
        return banner;
    }

    function insert() {
        var main = document.querySelector(".content main");
        if (!main || main.querySelector(".legacy-banner")) {
            return;
        }
        main.insertBefore(build(), main.firstChild);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", insert);
    } else {
        insert();
    }
})();

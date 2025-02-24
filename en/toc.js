// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded "><a href="about_AUTD3.html"><strong aria-hidden="true">1.</strong> About AUTD3</a></li><li class="chapter-item expanded "><a href="Users_Manual/users_manual.html"><strong aria-hidden="true">2.</strong> User&#39;s Manual</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/concept.html"><strong aria-hidden="true">2.1.</strong> Concept</a></li><li class="chapter-item "><a href="Users_Manual/getting_started.html"><strong aria-hidden="true">2.2.</strong> Tutorial</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/getting_started/rust.html"><strong aria-hidden="true">2.2.1.</strong> Rust</a></li><li class="chapter-item "><a href="Users_Manual/getting_started/cpp.html"><strong aria-hidden="true">2.2.2.</strong> C++</a></li><li class="chapter-item "><a href="Users_Manual/getting_started/cs.html"><strong aria-hidden="true">2.2.3.</strong> C#</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/getting_started/unity.html"><strong aria-hidden="true">2.2.3.1.</strong> Unity</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/getting_started/python.html"><strong aria-hidden="true">2.2.4.</strong> Python</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/versioning.html"><strong aria-hidden="true">2.3.</strong> Versioning</a></li><li class="chapter-item "><a href="Users_Manual/geometry.html"><strong aria-hidden="true">2.4.</strong> Geometry</a></li><li class="chapter-item "><a href="Users_Manual/link.html"><strong aria-hidden="true">2.5.</strong> Link</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/link/twincat.html"><strong aria-hidden="true">2.5.1.</strong> TwinCAT</a></li><li class="chapter-item "><a href="Users_Manual/link/soem.html"><strong aria-hidden="true">2.5.2.</strong> SOEM</a></li><li class="chapter-item "><a href="Users_Manual/link/simulator.html"><strong aria-hidden="true">2.5.3.</strong> Simulator</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/gain.html"><strong aria-hidden="true">2.6.</strong> Gain</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/gain/null.html"><strong aria-hidden="true">2.6.1.</strong> Null</a></li><li class="chapter-item "><a href="Users_Manual/gain/focus.html"><strong aria-hidden="true">2.6.2.</strong> Focus</a></li><li class="chapter-item "><a href="Users_Manual/gain/bessel.html"><strong aria-hidden="true">2.6.3.</strong> Bessel</a></li><li class="chapter-item "><a href="Users_Manual/gain/plane.html"><strong aria-hidden="true">2.6.4.</strong> Plane</a></li><li class="chapter-item "><a href="Users_Manual/gain/uniform.html"><strong aria-hidden="true">2.6.5.</strong> Uniform</a></li><li class="chapter-item "><a href="Users_Manual/gain/grouped.html"><strong aria-hidden="true">2.6.6.</strong> Group</a></li><li class="chapter-item "><a href="Users_Manual/gain/holo.html"><strong aria-hidden="true">2.6.7.</strong> Holo</a></li><li class="chapter-item "><a href="Users_Manual/gain/cache.html"><strong aria-hidden="true">2.6.8.</strong> Cache</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/modulation.html"><strong aria-hidden="true">2.7.</strong> Modulation</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/modulation/static.html"><strong aria-hidden="true">2.7.1.</strong> Static</a></li><li class="chapter-item "><a href="Users_Manual/modulation/sine.html"><strong aria-hidden="true">2.7.2.</strong> Sine</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/modulation/fourier.html"><strong aria-hidden="true">2.7.2.1.</strong> Fourier</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/modulation/square.html"><strong aria-hidden="true">2.7.3.</strong> Square</a></li><li class="chapter-item "><a href="Users_Manual/modulation/wav.html"><strong aria-hidden="true">2.7.4.</strong> Wav</a></li><li class="chapter-item "><a href="Users_Manual/modulation/cache.html"><strong aria-hidden="true">2.7.5.</strong> Cache</a></li><li class="chapter-item "><a href="Users_Manual/modulation/radiation.html"><strong aria-hidden="true">2.7.6.</strong> Radiation</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/stm.html"><strong aria-hidden="true">2.8.</strong> Spatio-Temporal Modulation</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/stm/focus.html"><strong aria-hidden="true">2.8.1.</strong> FociSTM</a></li><li class="chapter-item "><a href="Users_Manual/stm/gain.html"><strong aria-hidden="true">2.8.2.</strong> GainSTM</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/silencer.html"><strong aria-hidden="true">2.9.</strong> Silencer</a></li><li class="chapter-item "><a href="Users_Manual/controller.html"><strong aria-hidden="true">2.10.</strong> Controller</a></li><li class="chapter-item "><a href="Users_Manual/advanced_examples/advanced_examples.html"><strong aria-hidden="true">2.11.</strong> Advanced examples</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/advanced_examples/custom_gain.html"><strong aria-hidden="true">2.11.1.</strong> Custom Gain</a></li><li class="chapter-item "><a href="Users_Manual/advanced_examples/custom_modulation.html"><strong aria-hidden="true">2.11.2.</strong> Custom Modulation</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/Simulator/simulator.html"><strong aria-hidden="true">2.12.</strong> Simulaotr</a></li><li class="chapter-item "><a href="Users_Manual/FAQ/faq.html"><strong aria-hidden="true">2.13.</strong> FAQ</a></li><li class="chapter-item "><a href="Users_Manual/Citation/citation.html"><strong aria-hidden="true">2.14.</strong> Citation</a></li><li class="chapter-item "><a href="Users_Manual/LICENSE.html"><strong aria-hidden="true">2.15.</strong> License</a></li><li class="chapter-item "><a href="Users_Manual/release_notes.html"><strong aria-hidden="true">2.16.</strong> Release notes</a></li></ol></li><li class="chapter-item expanded "><a href="document_history.html"><strong aria-hidden="true">3.</strong> Document history</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0];
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);

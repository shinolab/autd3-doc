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
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded "><a href="about_AUTD3.html"><strong aria-hidden="true">1.</strong> About AUTD3</a></li><li class="chapter-item expanded "><div><strong aria-hidden="true">2.</strong> User Manual</div><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item expanded "><a href="Users_Manual/getting_started.html"><strong aria-hidden="true">2.1.</strong> Getting Started</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/getting_started/hardware.html"><strong aria-hidden="true">2.1.1.</strong> Hardware</a></li><li class="chapter-item "><a href="Users_Manual/getting_started/firmware.html"><strong aria-hidden="true">2.1.2.</strong> Firmware</a></li><li class="chapter-item "><a href="Users_Manual/getting_started/software.html"><strong aria-hidden="true">2.1.3.</strong> Software</a></li></ol></li><li class="chapter-item expanded "><a href="Users_Manual/tutorial.html"><strong aria-hidden="true">2.2.</strong> Tutorial</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/tutorial/single.html"><strong aria-hidden="true">2.2.1.</strong> Single Device</a></li><li class="chapter-item "><a href="Users_Manual/tutorial/multiple.html"><strong aria-hidden="true">2.2.2.</strong> Multiple Devices</a></li></ol></li><li class="chapter-item expanded "><a href="Users_Manual/concept.html"><strong aria-hidden="true">2.3.</strong> Concept</a></li><li class="chapter-item expanded "><div><strong aria-hidden="true">2.4.</strong> APIs</div><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/API/geometry.html"><strong aria-hidden="true">2.4.1.</strong> Geometry</a></li><li class="chapter-item "><a href="Users_Manual/API/link.html"><strong aria-hidden="true">2.4.2.</strong> Link</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/API/link/twincat.html"><strong aria-hidden="true">2.4.2.1.</strong> TwinCAT</a></li><li class="chapter-item "><a href="Users_Manual/API/link/ethercrab.html"><strong aria-hidden="true">2.4.2.2.</strong> EtherCrab</a></li><li class="chapter-item "><a href="Users_Manual/API/link/remote.html"><strong aria-hidden="true">2.4.2.3.</strong> Remote</a></li><li class="chapter-item "><a href="Users_Manual/API/link/remote_twincat.html"><strong aria-hidden="true">2.4.2.4.</strong> RemoteTwinCAT</a></li><li class="chapter-item "><a href="Users_Manual/API/link/soem.html"><strong aria-hidden="true">2.4.2.5.</strong> SOEM</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/API/controller.html"><strong aria-hidden="true">2.4.3.</strong> Controller</a></li><li class="chapter-item "><a href="Users_Manual/API/gain.html"><strong aria-hidden="true">2.4.4.</strong> Gain</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/API/gain/null.html"><strong aria-hidden="true">2.4.4.1.</strong> Null</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/focus.html"><strong aria-hidden="true">2.4.4.2.</strong> Focus</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/bessel.html"><strong aria-hidden="true">2.4.4.3.</strong> Bessel</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/plane.html"><strong aria-hidden="true">2.4.4.4.</strong> Plane</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/uniform.html"><strong aria-hidden="true">2.4.4.5.</strong> Uniform</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/custom.html"><strong aria-hidden="true">2.4.4.6.</strong> Custom</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/grouped.html"><strong aria-hidden="true">2.4.4.7.</strong> GainGroup</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/holo.html"><strong aria-hidden="true">2.4.4.8.</strong> Holo</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/API/gain/holo/naive.html"><strong aria-hidden="true">2.4.4.8.1.</strong> Naive</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/holo/gs.html"><strong aria-hidden="true">2.4.4.8.2.</strong> GS</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/holo/gspat.html"><strong aria-hidden="true">2.4.4.8.3.</strong> GSPAT</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/holo/lm.html"><strong aria-hidden="true">2.4.4.8.4.</strong> LM</a></li><li class="chapter-item "><a href="Users_Manual/API/gain/holo/greedy.html"><strong aria-hidden="true">2.4.4.8.5.</strong> Greedy</a></li></ol></li></ol></li><li class="chapter-item "><a href="Users_Manual/API/stm.html"><strong aria-hidden="true">2.4.5.</strong> STM/Spatio-Temporal Modulation</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/API/stm/focus.html"><strong aria-hidden="true">2.4.5.1.</strong> FociSTM</a></li><li class="chapter-item "><a href="Users_Manual/API/stm/gain.html"><strong aria-hidden="true">2.4.5.2.</strong> GainSTM</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/API/modulation.html"><strong aria-hidden="true">2.4.6.</strong> Modulation</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/API/modulation/static.html"><strong aria-hidden="true">2.4.6.1.</strong> Static</a></li><li class="chapter-item "><a href="Users_Manual/API/modulation/sine.html"><strong aria-hidden="true">2.4.6.2.</strong> Sine</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/API/modulation/fourier.html"><strong aria-hidden="true">2.4.6.2.1.</strong> Fourier</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/API/modulation/square.html"><strong aria-hidden="true">2.4.6.3.</strong> Square</a></li><li class="chapter-item "><a href="Users_Manual/API/modulation/custom.html"><strong aria-hidden="true">2.4.6.4.</strong> Custom</a></li><li class="chapter-item "><a href="Users_Manual/API/modulation/radiation.html"><strong aria-hidden="true">2.4.6.5.</strong> Radiation</a></li><li class="chapter-item "><a href="Users_Manual/API/modulation/fir.html"><strong aria-hidden="true">2.4.6.6.</strong> Fir</a></li></ol></li><li class="chapter-item "><a href="Users_Manual/API/sampling_config.html"><strong aria-hidden="true">2.4.7.</strong> SamplingConfig</a></li><li class="chapter-item "><a href="Users_Manual/API/segment.html"><strong aria-hidden="true">2.4.8.</strong> Segment/FiniteLoop</a></li><li class="chapter-item "><a href="Users_Manual/API/silencer.html"><strong aria-hidden="true">2.4.9.</strong> Silencer</a></li><li class="chapter-item "><a href="Users_Manual/API/phase_corr.html"><strong aria-hidden="true">2.4.10.</strong> PhaseCorrection</a></li><li class="chapter-item "><a href="Users_Manual/API/output_mask.html"><strong aria-hidden="true">2.4.11.</strong> OutputMask</a></li><li class="chapter-item "><a href="Users_Manual/API/pulse_width_encoder.html"><strong aria-hidden="true">2.4.12.</strong> PulseWidthEncoder</a></li><li class="chapter-item "><a href="Users_Manual/API/gpio_out.html"><strong aria-hidden="true">2.4.13.</strong> GPIOOutputs</a></li><li class="chapter-item "><a href="Users_Manual/API/fan.html"><strong aria-hidden="true">2.4.14.</strong> ForceFan</a></li><li class="chapter-item "><a href="Users_Manual/API/group.html"><strong aria-hidden="true">2.4.15.</strong> Group</a></li></ol></li><li class="chapter-item expanded "><a href="Users_Manual/Simulator/simulator.html"><strong aria-hidden="true">2.5.</strong> Simulator</a></li><li class="chapter-item expanded "><a href="Users_Manual/Emulator/emulator.html"><strong aria-hidden="true">2.6.</strong> Emulator</a></li><li class="chapter-item expanded "><a href="Users_Manual/advanced.html"><strong aria-hidden="true">2.7.</strong> Advanced Topics</a><a class="toggle"><div>❱</div></a></li><li><ol class="section"><li class="chapter-item "><a href="Users_Manual/advanced/custom_gain.html"><strong aria-hidden="true">2.7.1.</strong> Custom Gain</a></li><li class="chapter-item "><a href="Users_Manual/advanced/custom_modulation.html"><strong aria-hidden="true">2.7.2.</strong> Custom Modulation</a></li><li class="chapter-item "><a href="Users_Manual/advanced/remote_server.html"><strong aria-hidden="true">2.7.3.</strong> Building a Remote Server</a></li></ol></li><li class="chapter-item expanded "><a href="Users_Manual/versioning.html"><strong aria-hidden="true">2.8.</strong> Versioning</a></li><li class="chapter-item expanded "><a href="Users_Manual/FAQ/faq.html"><strong aria-hidden="true">2.9.</strong> FAQ</a></li><li class="chapter-item expanded "><a href="Users_Manual/Citation/citation.html"><strong aria-hidden="true">2.10.</strong> Citation</a></li><li class="chapter-item expanded "><a href="Users_Manual/LICENSE.html"><strong aria-hidden="true">2.11.</strong> License</a></li><li class="chapter-item expanded "><a href="Users_Manual/release_notes.html"><strong aria-hidden="true">2.12.</strong> Release Notes</a></li></ol></li><li class="chapter-item expanded "><a href="document_history.html"><strong aria-hidden="true">3.</strong> Document History</a></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split("#")[0].split("?")[0];
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

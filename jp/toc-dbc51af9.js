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
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="about_AUTD3.html"><strong aria-hidden="true">1.</strong> AUTD3について</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><span><strong aria-hidden="true">2.</strong> ユーザーズマニュアル</span><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/getting_started.html"><strong aria-hidden="true">2.1.</strong> はじめに</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/getting_started/hardware.html"><strong aria-hidden="true">2.1.1.</strong> ハードウェア</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/getting_started/firmware.html"><strong aria-hidden="true">2.1.2.</strong> ファームウェア</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/getting_started/software.html"><strong aria-hidden="true">2.1.3.</strong> ソフトウェア</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/tutorial.html"><strong aria-hidden="true">2.2.</strong> チュートリアル</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/tutorial/single.html"><strong aria-hidden="true">2.2.1.</strong> 単一デバイスの駆動</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/tutorial/multiple.html"><strong aria-hidden="true">2.2.2.</strong> 複数デバイスの接続</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/tutorial/concept.html"><strong aria-hidden="true">2.2.3.</strong> コンセプト</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/tutorial/move_focus.html"><strong aria-hidden="true">2.2.4.</strong> 焦点の移動</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/tutorial/silencer.html"><strong aria-hidden="true">2.2.5.</strong> 静音化</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/tutorial/intensity.html"><strong aria-hidden="true">2.2.6.</strong> 出力音圧の制御</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/tutorial/segment.html"><strong aria-hidden="true">2.2.7.</strong> Segmentの使用</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><span><strong aria-hidden="true">2.3.</strong> APIs</span><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/link.html"><strong aria-hidden="true">2.3.1.</strong> Link</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/link/twincat.html"><strong aria-hidden="true">2.3.1.1.</strong> TwinCAT</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/link/ethercrab.html"><strong aria-hidden="true">2.3.1.2.</strong> EtherCrab</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/link/remote.html"><strong aria-hidden="true">2.3.1.3.</strong> Remote</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/link/remote_twincat.html"><strong aria-hidden="true">2.3.1.4.</strong> RemoteTwinCAT</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/link/soem.html"><strong aria-hidden="true">2.3.1.5.</strong> SOEM</a></span></li></ol><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/controller.html"><strong aria-hidden="true">2.3.2.</strong> Controller</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/geometry.html"><strong aria-hidden="true">2.3.2.1.</strong> Geometry</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/environment.html"><strong aria-hidden="true">2.3.2.2.</strong> Environment</a></span></li></ol><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain.html"><strong aria-hidden="true">2.3.3.</strong> Gain</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/null.html"><strong aria-hidden="true">2.3.3.1.</strong> Null</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/focus.html"><strong aria-hidden="true">2.3.3.2.</strong> Focus</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/bessel.html"><strong aria-hidden="true">2.3.3.3.</strong> Bessel</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/plane.html"><strong aria-hidden="true">2.3.3.4.</strong> Plane</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/uniform.html"><strong aria-hidden="true">2.3.3.5.</strong> Uniform</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/custom.html"><strong aria-hidden="true">2.3.3.6.</strong> Custom</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/grouped.html"><strong aria-hidden="true">2.3.3.7.</strong> GainGroup</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/holo.html"><strong aria-hidden="true">2.3.3.8.</strong> Holo</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/holo/naive.html"><strong aria-hidden="true">2.3.3.8.1.</strong> Naive</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/holo/gs.html"><strong aria-hidden="true">2.3.3.8.2.</strong> GS</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/holo/gspat.html"><strong aria-hidden="true">2.3.3.8.3.</strong> GSPAT</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gain/holo/greedy.html"><strong aria-hidden="true">2.3.3.8.4.</strong> Greedy</a></span></li></ol></li></ol><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/stm.html"><strong aria-hidden="true">2.3.4.</strong> STM/Spatio-Temporal Modulation</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/stm/focus.html"><strong aria-hidden="true">2.3.4.1.</strong> FociSTM</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/stm/gain.html"><strong aria-hidden="true">2.3.4.2.</strong> GainSTM</a></span></li></ol><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/modulation.html"><strong aria-hidden="true">2.3.5.</strong> Modulation</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/modulation/static.html"><strong aria-hidden="true">2.3.5.1.</strong> Static</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/modulation/sine.html"><strong aria-hidden="true">2.3.5.2.</strong> Sine</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/modulation/fourier.html"><strong aria-hidden="true">2.3.5.2.1.</strong> Fourier</a></span></li></ol><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/modulation/square.html"><strong aria-hidden="true">2.3.5.3.</strong> Square</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/modulation/custom.html"><strong aria-hidden="true">2.3.5.4.</strong> Custom</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/modulation/radiation.html"><strong aria-hidden="true">2.3.5.5.</strong> Radiation</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/modulation/fir.html"><strong aria-hidden="true">2.3.5.6.</strong> Fir</a></span></li></ol><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/sampling_config.html"><strong aria-hidden="true">2.3.6.</strong> SamplingConfig</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/segment.html"><strong aria-hidden="true">2.3.7.</strong> Segment/FiniteLoop</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/silencer.html"><strong aria-hidden="true">2.3.8.</strong> Silencer</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/phase_corr.html"><strong aria-hidden="true">2.3.9.</strong> PhaseCorrection/位相補正</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/output_mask.html"><strong aria-hidden="true">2.3.10.</strong> OutputMask/出力マスク</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/pulse_width_encoder.html"><strong aria-hidden="true">2.3.11.</strong> PulseWidthEncoder/振幅とパルス幅</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/gpio_out.html"><strong aria-hidden="true">2.3.12.</strong> GPIOOutputs/GPIO出力設定</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/fan.html"><strong aria-hidden="true">2.3.13.</strong> ForceFan/ファン制御</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/API/group.html"><strong aria-hidden="true">2.3.14.</strong> Group</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/Simulator/simulator.html"><strong aria-hidden="true">2.4.</strong> シミュレータ</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/Emulator/emulator.html"><strong aria-hidden="true">2.5.</strong> エミュレータ</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/advanced.html"><strong aria-hidden="true">2.6.</strong> 高度なトピック</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/advanced/custom_gain.html"><strong aria-hidden="true">2.6.1.</strong> Gainの自作</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/advanced/custom_modulation.html"><strong aria-hidden="true">2.6.2.</strong> Modulationの自作</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Users_Manual/advanced/remote_server.html"><strong aria-hidden="true">2.6.3.</strong> リモートサーバの構築</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/versioning.html"><strong aria-hidden="true">2.7.</strong> バージョニング</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/FAQ/faq.html"><strong aria-hidden="true">2.8.</strong> FAQ</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/Citation/citation.html"><strong aria-hidden="true">2.9.</strong> 引用</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/LICENSE.html"><strong aria-hidden="true">2.10.</strong> ライセンス</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Users_Manual/release_notes.html"><strong aria-hidden="true">2.11.</strong> リリースノート</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Developer_Manual/Developer_manual.html"><strong aria-hidden="true">3.</strong> デベロッパーズマニュアル</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga.html"><strong aria-hidden="true">3.1.</strong> FPGAファームウェア</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/develop.html"><strong aria-hidden="true">3.1.1.</strong> 開発環境構築</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/overview.html"><strong aria-hidden="true">3.1.2.</strong> 概要</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/pwm.html"><strong aria-hidden="true">3.1.3.</strong> PWM</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/pulse_width_encoder.html"><strong aria-hidden="true">3.1.4.</strong> Pulse Witdth Encoder</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/silencer.html"><strong aria-hidden="true">3.1.5.</strong> Silencer</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/modulation.html"><strong aria-hidden="true">3.1.6.</strong> Modulation</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/phase_corr.html"><strong aria-hidden="true">3.1.7.</strong> Phase Correction</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/stm.html"><strong aria-hidden="true">3.1.8.</strong> STM</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/sync.html"><strong aria-hidden="true">3.1.9.</strong> Synchronizer</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/time_cnt.html"><strong aria-hidden="true">3.1.10.</strong> Time Count Generator</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/controller.html"><strong aria-hidden="true">3.1.11.</strong> Controller</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/memory.html"><strong aria-hidden="true">3.1.12.</strong> Memory</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/fpga/cpu_interface.html"><strong aria-hidden="true">3.1.12.1.</strong> CPUボードとのインターフェース</a></span></li></ol></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Developer_Manual/cpu.html"><strong aria-hidden="true">3.2.</strong> CPUファームウェア</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Developer_Manual/cpu/develop.html"><strong aria-hidden="true">3.2.1.</strong> 開発環境構築</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Developer_Manual/software.html"><strong aria-hidden="true">3.3.</strong> ソフトウェア</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Theory/theory.html"><strong aria-hidden="true">4.</strong> 理論と考察</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Theory/pwm.html"><strong aria-hidden="true">4.1.</strong> PWM</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Theory/phasedarray.html"><strong aria-hidden="true">4.2.</strong> フェーズドアレイについて</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Theory/linear.html"><strong aria-hidden="true">4.3.</strong> フェーズドアレイの線形性</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Theory/resolution.html"><strong aria-hidden="true">4.4.</strong> 分解能に関する考察</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Theory/holo/holo.html"><strong aria-hidden="true">4.5.</strong> 多焦点生成</a><a class="chapter-fold-toggle"><div>❱</div></a></span><ol class="section"><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Theory/holo/partitioning.html"><strong aria-hidden="true">4.5.1.</strong> 空間分割スキーム</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Theory/holo/fourier.html"><strong aria-hidden="true">4.5.2.</strong> 逆フーリエ変換</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Theory/holo/sdp.html"><strong aria-hidden="true">4.5.3.</strong> 半正定値緩和法</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Theory/holo/evp.html"><strong aria-hidden="true">4.5.4.</strong> 固有値問題と行列方程式</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Theory/holo/back_prop.html"><strong aria-hidden="true">4.5.5.</strong> 逆伝搬法</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Theory/holo/nlsp.html"><strong aria-hidden="true">4.5.6.</strong> 非線形最小二乗法</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Theory/holo/apo.html"><strong aria-hidden="true">4.5.7.</strong> 音響パワー最適化法</a></span></li><li class="chapter-item "><span class="chapter-link-wrapper"><a href="Theory/holo/greedy.html"><strong aria-hidden="true">4.5.8.</strong> 貪欲法</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Theory/multi-freq.html"><strong aria-hidden="true">4.6.</strong> 複数周波数の応用</a></span></li><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="Theory/radiation_pressure.html"><strong aria-hidden="true">4.7.</strong> 音響放射圧</a></span></li></ol><li class="chapter-item expanded "><span class="chapter-link-wrapper"><a href="document_history.html"><strong aria-hidden="true">5.</strong> ドキュメント履歴</a></span></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString().split('#')[0].split('?')[0];
        if (current_page.endsWith('/')) {
            current_page += 'index.html';
        }
        const links = Array.prototype.slice.call(this.querySelectorAll('a'));
        const l = links.length;
        for (let i = 0; i < l; ++i) {
            const link = links[i];
            const href = link.getAttribute('href');
            if (href && !href.startsWith('#') && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The 'index' page is supposed to alias the first chapter in the book.
            if (link.href === current_page
                || i === 0
                && path_to_root === ''
                && current_page.endsWith('/index.html')) {
                link.classList.add('active');
                let parent = link.parentElement;
                while (parent) {
                    if (parent.tagName === 'LI' && parent.classList.contains('chapter-item')) {
                        parent.classList.add('expanded');
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', e => {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        const sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via
            // 'next/previous chapter' buttons
            const activeSection = document.querySelector('#mdbook-sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        const sidebarAnchorToggles = document.querySelectorAll('.chapter-fold-toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(el => {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define('mdbook-sidebar-scrollbox', MDBookSidebarScrollbox);


// ---------------------------------------------------------------------------
// Support for dynamically adding headers to the sidebar.

(function() {
    // This is used to detect which direction the page has scrolled since the
    // last scroll event.
    let lastKnownScrollPosition = 0;
    // This is the threshold in px from the top of the screen where it will
    // consider a header the "current" header when scrolling down.
    const defaultDownThreshold = 150;
    // Same as defaultDownThreshold, except when scrolling up.
    const defaultUpThreshold = 300;
    // The threshold is a virtual horizontal line on the screen where it
    // considers the "current" header to be above the line. The threshold is
    // modified dynamically to handle headers that are near the bottom of the
    // screen, and to slightly offset the behavior when scrolling up vs down.
    let threshold = defaultDownThreshold;
    // This is used to disable updates while scrolling. This is needed when
    // clicking the header in the sidebar, which triggers a scroll event. It
    // is somewhat finicky to detect when the scroll has finished, so this
    // uses a relatively dumb system of disabling scroll updates for a short
    // time after the click.
    let disableScroll = false;
    // Array of header elements on the page.
    let headers;
    // Array of li elements that are initially collapsed headers in the sidebar.
    // I'm not sure why eslint seems to have a false positive here.
    // eslint-disable-next-line prefer-const
    let headerToggles = [];
    // This is a debugging tool for the threshold which you can enable in the console.
    let thresholdDebug = false;

    // Updates the threshold based on the scroll position.
    function updateThreshold() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;

        // The number of pixels below the viewport, at most documentHeight.
        // This is used to push the threshold down to the bottom of the page
        // as the user scrolls towards the bottom.
        const pixelsBelow = Math.max(0, documentHeight - (scrollTop + windowHeight));
        // The number of pixels above the viewport, at least defaultDownThreshold.
        // Similar to pixelsBelow, this is used to push the threshold back towards
        // the top when reaching the top of the page.
        const pixelsAbove = Math.max(0, defaultDownThreshold - scrollTop);
        // How much the threshold should be offset once it gets close to the
        // bottom of the page.
        const bottomAdd = Math.max(0, windowHeight - pixelsBelow - defaultDownThreshold);
        let adjustedBottomAdd = bottomAdd;

        // Adjusts bottomAdd for a small document. The calculation above
        // assumes the document is at least twice the windowheight in size. If
        // it is less than that, then bottomAdd needs to be shrunk
        // proportional to the difference in size.
        if (documentHeight < windowHeight * 2) {
            const maxPixelsBelow = documentHeight - windowHeight;
            const t = 1 - pixelsBelow / Math.max(1, maxPixelsBelow);
            const clamp = Math.max(0, Math.min(1, t));
            adjustedBottomAdd *= clamp;
        }

        let scrollingDown = true;
        if (scrollTop < lastKnownScrollPosition) {
            scrollingDown = false;
        }

        if (scrollingDown) {
            // When scrolling down, move the threshold up towards the default
            // downwards threshold position. If near the bottom of the page,
            // adjustedBottomAdd will offset the threshold towards the bottom
            // of the page.
            const amountScrolledDown = scrollTop - lastKnownScrollPosition;
            const adjustedDefault = defaultDownThreshold + adjustedBottomAdd;
            threshold = Math.max(adjustedDefault, threshold - amountScrolledDown);
        } else {
            // When scrolling up, move the threshold down towards the default
            // upwards threshold position. If near the bottom of the page,
            // quickly transition the threshold back up where it normally
            // belongs.
            const amountScrolledUp = lastKnownScrollPosition - scrollTop;
            const adjustedDefault = defaultUpThreshold - pixelsAbove
                + Math.max(0, adjustedBottomAdd - defaultDownThreshold);
            threshold = Math.min(adjustedDefault, threshold + amountScrolledUp);
        }

        if (documentHeight <= windowHeight) {
            threshold = 0;
        }

        if (thresholdDebug) {
            const id = 'mdbook-threshold-debug-data';
            let data = document.getElementById(id);
            if (data === null) {
                data = document.createElement('div');
                data.id = id;
                data.style.cssText = `
                    position: fixed;
                    top: 50px;
                    right: 10px;
                    background-color: 0xeeeeee;
                    z-index: 9999;
                    pointer-events: none;
                `;
                document.body.appendChild(data);
            }
            data.innerHTML = `
                <table>
                  <tr><td>documentHeight</td><td>${documentHeight.toFixed(1)}</td></tr>
                  <tr><td>windowHeight</td><td>${windowHeight.toFixed(1)}</td></tr>
                  <tr><td>scrollTop</td><td>${scrollTop.toFixed(1)}</td></tr>
                  <tr><td>pixelsAbove</td><td>${pixelsAbove.toFixed(1)}</td></tr>
                  <tr><td>pixelsBelow</td><td>${pixelsBelow.toFixed(1)}</td></tr>
                  <tr><td>bottomAdd</td><td>${bottomAdd.toFixed(1)}</td></tr>
                  <tr><td>adjustedBottomAdd</td><td>${adjustedBottomAdd.toFixed(1)}</td></tr>
                  <tr><td>scrollingDown</td><td>${scrollingDown}</td></tr>
                  <tr><td>threshold</td><td>${threshold.toFixed(1)}</td></tr>
                </table>
            `;
            drawDebugLine();
        }

        lastKnownScrollPosition = scrollTop;
    }

    function drawDebugLine() {
        if (!document.body) {
            return;
        }
        const id = 'mdbook-threshold-debug-line';
        const existingLine = document.getElementById(id);
        if (existingLine) {
            existingLine.remove();
        }
        const line = document.createElement('div');
        line.id = id;
        line.style.cssText = `
            position: fixed;
            top: ${threshold}px;
            left: 0;
            width: 100vw;
            height: 2px;
            background-color: red;
            z-index: 9999;
            pointer-events: none;
        `;
        document.body.appendChild(line);
    }

    function mdbookEnableThresholdDebug() {
        thresholdDebug = true;
        updateThreshold();
        drawDebugLine();
    }

    window.mdbookEnableThresholdDebug = mdbookEnableThresholdDebug;

    // Updates which headers in the sidebar should be expanded. If the current
    // header is inside a collapsed group, then it, and all its parents should
    // be expanded.
    function updateHeaderExpanded(currentA) {
        // Add expanded to all header-item li ancestors.
        let current = currentA.parentElement;
        while (current) {
            if (current.tagName === 'LI' && current.classList.contains('header-item')) {
                current.classList.add('expanded');
            }
            current = current.parentElement;
        }
    }

    // Updates which header is marked as the "current" header in the sidebar.
    // This is done with a virtual Y threshold, where headers at or below
    // that line will be considered the current one.
    function updateCurrentHeader() {
        if (!headers || !headers.length) {
            return;
        }

        // Reset the classes, which will be rebuilt below.
        const els = document.getElementsByClassName('current-header');
        for (const el of els) {
            el.classList.remove('current-header');
        }
        for (const toggle of headerToggles) {
            toggle.classList.remove('expanded');
        }

        // Find the last header that is above the threshold.
        let lastHeader = null;
        for (const header of headers) {
            const rect = header.getBoundingClientRect();
            if (rect.top <= threshold) {
                lastHeader = header;
            } else {
                break;
            }
        }
        if (lastHeader === null) {
            lastHeader = headers[0];
            const rect = lastHeader.getBoundingClientRect();
            const windowHeight = window.innerHeight;
            if (rect.top >= windowHeight) {
                return;
            }
        }

        // Get the anchor in the summary.
        const href = '#' + lastHeader.id;
        const a = [...document.querySelectorAll('.header-in-summary')]
            .find(element => element.getAttribute('href') === href);
        if (!a) {
            return;
        }

        a.classList.add('current-header');

        updateHeaderExpanded(a);
    }

    // Updates which header is "current" based on the threshold line.
    function reloadCurrentHeader() {
        if (disableScroll) {
            return;
        }
        updateThreshold();
        updateCurrentHeader();
    }


    // When clicking on a header in the sidebar, this adjusts the threshold so
    // that it is located next to the header. This is so that header becomes
    // "current".
    function headerThresholdClick(event) {
        // See disableScroll description why this is done.
        disableScroll = true;
        setTimeout(() => {
            disableScroll = false;
        }, 100);
        // requestAnimationFrame is used to delay the update of the "current"
        // header until after the scroll is done, and the header is in the new
        // position.
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                // Closest is needed because if it has child elements like <code>.
                const a = event.target.closest('a');
                const href = a.getAttribute('href');
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    threshold = targetElement.getBoundingClientRect().bottom;
                    updateCurrentHeader();
                }
            });
        });
    }

    // Takes the nodes from the given head and copies them over to the
    // destination, along with some filtering.
    function filterHeader(source, dest) {
        const clone = source.cloneNode(true);
        clone.querySelectorAll('mark').forEach(mark => {
            mark.replaceWith(...mark.childNodes);
        });
        dest.append(...clone.childNodes);
    }

    // Scans page for headers and adds them to the sidebar.
    document.addEventListener('DOMContentLoaded', function() {
        const activeSection = document.querySelector('#mdbook-sidebar .active');
        if (activeSection === null) {
            return;
        }

        const main = document.getElementsByTagName('main')[0];
        headers = Array.from(main.querySelectorAll('h2, h3, h4, h5, h6'))
            .filter(h => h.id !== '' && h.children.length && h.children[0].tagName === 'A');

        if (headers.length === 0) {
            return;
        }

        // Build a tree of headers in the sidebar.

        const stack = [];

        const firstLevel = parseInt(headers[0].tagName.charAt(1));
        for (let i = 1; i < firstLevel; i++) {
            const ol = document.createElement('ol');
            ol.classList.add('section');
            if (stack.length > 0) {
                stack[stack.length - 1].ol.appendChild(ol);
            }
            stack.push({level: i + 1, ol: ol});
        }

        // The level where it will start folding deeply nested headers.
        const foldLevel = 3;

        for (let i = 0; i < headers.length; i++) {
            const header = headers[i];
            const level = parseInt(header.tagName.charAt(1));

            const currentLevel = stack[stack.length - 1].level;
            if (level > currentLevel) {
                // Begin nesting to this level.
                for (let nextLevel = currentLevel + 1; nextLevel <= level; nextLevel++) {
                    const ol = document.createElement('ol');
                    ol.classList.add('section');
                    const last = stack[stack.length - 1];
                    const lastChild = last.ol.lastChild;
                    // Handle the case where jumping more than one nesting
                    // level, which doesn't have a list item to place this new
                    // list inside of.
                    if (lastChild) {
                        lastChild.appendChild(ol);
                    } else {
                        last.ol.appendChild(ol);
                    }
                    stack.push({level: nextLevel, ol: ol});
                }
            } else if (level < currentLevel) {
                while (stack.length > 1 && stack[stack.length - 1].level > level) {
                    stack.pop();
                }
            }

            const li = document.createElement('li');
            li.classList.add('header-item');
            li.classList.add('expanded');
            if (level < foldLevel) {
                li.classList.add('expanded');
            }
            const span = document.createElement('span');
            span.classList.add('chapter-link-wrapper');
            const a = document.createElement('a');
            span.appendChild(a);
            a.href = '#' + header.id;
            a.classList.add('header-in-summary');
            filterHeader(header.children[0], a);
            a.addEventListener('click', headerThresholdClick);
            const nextHeader = headers[i + 1];
            if (nextHeader !== undefined) {
                const nextLevel = parseInt(nextHeader.tagName.charAt(1));
                if (nextLevel > level && level >= foldLevel) {
                    const toggle = document.createElement('a');
                    toggle.classList.add('chapter-fold-toggle');
                    toggle.classList.add('header-toggle');
                    toggle.addEventListener('click', () => {
                        li.classList.toggle('expanded');
                    });
                    const toggleDiv = document.createElement('div');
                    toggleDiv.textContent = '❱';
                    toggle.appendChild(toggleDiv);
                    span.appendChild(toggle);
                    headerToggles.push(li);
                }
            }
            li.appendChild(span);

            const currentParent = stack[stack.length - 1];
            currentParent.ol.appendChild(li);
        }

        const onThisPage = document.createElement('div');
        onThisPage.classList.add('on-this-page');
        onThisPage.append(stack[0].ol);
        const activeItemSpan = activeSection.parentElement;
        activeItemSpan.after(onThisPage);
    });

    document.addEventListener('DOMContentLoaded', reloadCurrentHeader);
    document.addEventListener('scroll', reloadCurrentHeader, { passive: true });
})();


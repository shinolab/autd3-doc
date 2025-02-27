document.addEventListener('DOMContentLoaded', () => {
    const code = document.getElementsByTagName('code');
    Array.from(code).forEach(el => {
        if (el.className) {
            const tokens = el.className.split(' ');

            const language = tokens.find(c => c.startsWith('language-'));
            if (language) {
                const id = language.replace('language-', '');
                if (["rust", "cpp", "cs", "python"].includes(id)) {
                    el.parentElement.setAttribute('id', id + '_code_content');
                    el.parentElement.classList.add('tab_content');
                }
            }

            const filenameClass = tokens.find(c => c.startsWith('name='));
            if (filenameClass) {
                const filename = filenameClass.replace('name=', '');
                if (filename.length > 0) {
                    el.parentElement.setAttribute('name', filename);
                    el.parentElement.classList.add('code-block-header');
                }
            }
        }
    });
});

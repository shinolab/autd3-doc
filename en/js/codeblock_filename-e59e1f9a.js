document.addEventListener('DOMContentLoaded', () => {
    const code = document.getElementsByTagName('code');
    Array.from(code).forEach(el => {
        if (el.className) {
            const filenameClass = el.className.split(' ').find(c => c.startsWith('name='));
            if (filenameClass) {
                const filename = filenameClass.replace('name=', '');
                if (filename.length > 0) {
                    el.parentElement.setAttribute('name', filename);
                    el.parentElement.classList.add('code-block-header');
                }
            } else {
                const language = el.className.split(' ').find(c => c.startsWith('language-'));
                if (language) {
                    const name = language.replace('language-', '');
                    if (["shell"].includes(name)) {
                        el.parentElement.setAttribute('name', name);
                        el.parentElement.classList.add('code-block-header');
                    }
                }
            }
        }
    });
});

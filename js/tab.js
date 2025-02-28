
document.addEventListener('DOMContentLoaded', () => {
    const code = document.getElementsByTagName('code');
    Array.from(code).forEach(el => {
        if (el.className) {
            const language = el.className.split(' ').find(c => c.startsWith('language-'));
            if (language) {
                const id = language.replace('language-', '');
                if (["rust", "cpp", "cs", "python"].includes(id)) {
                    el.parentElement.setAttribute('id', id + '_code_content');
                    el.parentElement.classList.add('tab_content');
                }
            }
        }
    });
});

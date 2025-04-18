# AUTD3 User's Guide

## Build with Docker

```
git clone https://github.com/shinolab/autd3-doc.git
cd autd3-doc
docker build -f ./Dockerfile . -t autd3-book:1.0
docker run -it --rm -d -e MDBOOK_BOOK__src=src/en --name autd3-book -p 3300:3000 --hostname="mdbook" autd3-book:1.0 mdbook serve -p 3000 -n mdbook
```

Then open [`http://localhost:3300`](http://localhost:3300) in your browser.

- If you want to build a Japanese version, run
    ```
    docker run -it --rm -d -e MDBOOK_BOOK__src=src/jp --name autd3-book -p 3300:3000 --hostname="mdbook" autd3-book:1.0 mdbook serve -p 3000 -n mdbook
    ```

## Build with mdbook

To build this book on your local machine, you need to install the following tools:
- [mdbook](https://github.com/rust-lang/mdBook)
- [mdbook-katex](https://github.com/lzanini/mdbook-katex)
- [mdbook-toc](https://github.com/badboy/mdbook-toc)
- [mdbook-open-on-gh](https://github.com/badboy/mdbook-open-on-gh)
- [mdbook-inpage-tab](https://github.com/shinolab/mdbook-inpage-tab)

Then, run the following command:

```bash
git clone https://github.com/shinolab/autd3-doc.git
cd autd3-doc
MDBOOK_BOOK__src=src/en mdbook serve --open
```

- If you want to build a Japanese version, run
    ```bash
    MDBOOK_BOOK__src=src/jp mdbook serve --open
    ```

# Author

Shun Suzuki, 2022-2025

FROM rust:1.70-alpine

ARG mdbook_dir=/home
ARG mdbook_url=https://github.com/rust-lang/mdBook/releases/download/v0.4.48/mdbook-v0.4.48-x86_64-unknown-linux-musl.tar.gz
ARG mdbook_toc_url=https://github.com/badboy/mdbook-toc/releases/download/0.14.2/mdbook-toc-0.14.2-x86_64-unknown-linux-musl.tar.gz
ARG mdbook_katex_url=https://github.com/lzanini/mdbook-katex/releases/download/0.9.3-binaries/mdbook-katex-v0.9.3-x86_64-unknown-linux-musl.tar.gz
ARG mdbook_open_on_gh_url=https://github.com/badboy/mdbook-open-on-gh/releases/download/2.4.3/mdbook-open-on-gh-2.4.3-x86_64-unknown-linux-musl.tar.gz
ARG mdbook_inpage_tab=https://github.com/shinolab/mdbook-inpage-tab/releases/download/v0.1.2/mdbook-inpage-tab-v0.1.2-x86_64-unknown-linux-musl.tar.gz

WORKDIR ${mdbook_dir}
RUN wget ${mdbook_url} -O mdbook.tar.gz && \
    tar xf mdbook.tar.gz && \
    chmod +x ./mdbook && \
    mv ./mdbook /usr/local/bin/mdbook && \
    rm mdbook.tar.gz
RUN wget ${mdbook_toc_url} -O mdbook-toc.tar.gz && \
    tar xf mdbook-toc.tar.gz && \
    chmod +x ./mdbook-toc && \
    mv ./mdbook-toc /usr/local/bin/mdbook-toc && \
    rm mdbook-toc.tar.gz
RUN wget ${mdbook_katex_url} -O mdbook-katex.tar.gz && \
    tar xf mdbook-katex.tar.gz && \
    chmod +x ./mdbook-katex && \
    mv ./mdbook-katex /usr/local/bin/mdbook-katex && \
    rm mdbook-katex.tar.gz
RUN wget ${mdbook_open_on_gh_url} -O mdbook-open-on-gh.tar.gz && \
    tar xf mdbook-open-on-gh.tar.gz && \
    chmod +x ./mdbook-open-on-gh && \
    mv ./mdbook-open-on-gh /usr/local/bin/mdbook-open-on-gh && \
    rm mdbook-open-on-gh.tar.gz
RUN wget ${mdbook_inpage_tab} -O mdbook-inpage-tab.tar.gz && \
    tar xf mdbook-inpage-tab.tar.gz && \
    chmod +x ./mdbook-inpage-tab && \
    mv ./mdbook-inpage-tab /usr/local/bin/mdbook-inpage-tab && \
    rm mdbook-inpage-tab.tar.gz

COPY .git/ .git/
COPY book.toml .
COPY katex_macro.txt .
COPY src/ src/
COPY css/ css/
COPY js/ js/

EXPOSE 3000

# Awesome Standard ML [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources for the [Standard ML](https://en.wikipedia.org/wiki/Standard_ML) programming language, plus a complete index of the sjqtentacles pure-SML library ecosystem.

Standard ML is a statically typed functional language with a formally defined
semantics (The Definition of Standard ML), type inference, parametric
polymorphism, and an expressive module system. This list collects compilers,
learning resources, and tooling for the wider community, followed by an
auto-generated catalog of the sjqtentacles ecosystem: 330+ small, pure,
dependency-free libraries that build byte-identically under both MLton and
Poly/ML. See also the [dependency graph](dependency-graph.md) of how the
ecosystem libraries depend on each other.

<!-- The section below is generated from data/ by scripts/generate.py. Do not edit by hand. -->
<!-- BEGIN GENERATED -->
## Contents

- [Compilers & runtimes](#compilers--runtimes)
- [Language standard & evolution](#language-standard--evolution)
- [Learning resources](#learning-resources)
- [Tooling (community)](#tooling-community)
- [Editor support](#editor-support)
- [Other lists & indexes](#other-lists--indexes)
- [sjqtentacles ecosystem](#sjqtentacles-ecosystem)
  - [Developer tooling (SML self-tooling)](#developer-tooling-sml-self-tooling)
  - [Cryptography & security](#cryptography--security)
  - [Blockchain & cryptocurrency](#blockchain--cryptocurrency)
  - [Media containers & codecs](#media-containers--codecs)
  - [Encoding, serialization & compression](#encoding-serialization--compression)
  - [Web, networking & protocols](#web-networking--protocols)
  - [Parsing & languages](#parsing--languages)
  - [Information retrieval & NLP](#information-retrieval--nlp)
  - [Formal methods & logic](#formal-methods--logic)
  - [Math, numeric & scientific](#math-numeric--scientific)
  - [Data structures](#data-structures)
  - [Algorithms](#algorithms)
  - [Graphics, geometry & imaging](#graphics-geometry--imaging)
  - [Audio & music](#audio--music)
  - [Games & simulation](#games--simulation)
  - [Concurrency, effects & systems](#concurrency-effects--systems)
  - [Databases & storage](#databases--storage)
  - [GUI, terminal & application UI](#gui-terminal--application-ui)
  - [Text, Unicode & utilities](#text-unicode--utilities)
  - [Misc](#misc)

## Compilers & runtimes

Implementations of Standard ML you can actually run code with.

- [MLton](http://mlton.org/) - A whole-program optimizing compiler producing fast standalone native executables. The de-facto target for performance-sensitive SML.
- [Standard ML of New Jersey (SML/NJ)](https://www.smlnj.org/) - A mature compiler and interactive system with a large library and the Compilation Manager (CM).
- [Poly/ML](https://www.polyml.org/) - A full implementation with a fast incremental compiler and REPL; the implementation language of the Isabelle theorem prover.
- [MLKit](https://www.elsman.com/mlkit/) - A compiler emphasizing region-based memory management and full Definition compliance.
- [Moscow ML](https://mosml.org/) - A lightweight implementation based on the CAML runtime, with interactive and batch use.
- [HaMLet](https://people.mpi-sws.org/~rossberg/hamlet/) - A faithful, reference-style implementation of the SML Definition, intended as executable specification.
- [SOSML](https://sosml.org/) - An in-browser SML interpreter, handy for teaching and quick tries.

## Language standard & evolution

The Definition and ongoing successor-language work.

- [The Definition of Standard ML (Revised)](https://mitpress.mit.edu/9780262631815/the-definition-of-standard-ml/) - The formal semantics of the language (Milner, Tofte, Harper, MacQueen).
- [Successor ML (sML)](https://github.com/SMLFamily/Successor-ML) - A community effort collecting incremental, backward-compatible improvements to the language.
- [SML Family GitHub](https://github.com/SMLFamily) - Home of the Basis Library spec and successor-ML discussion.

## Learning resources

Books, courses and tutorials for learning Standard ML.

- [ML for the Working Programmer (Paulson)](https://www.cl.cam.ac.uk/~lp15/MLbook/) - A classic, practical introduction to programming in ML.
- [Programming in Standard ML (Harper)](https://www.cs.cmu.edu/~rwh/isml/book.pdf) - Robert Harper's free textbook used at Carnegie Mellon.
- [CMU 15-150: Principles of Functional Programming](https://www.cs.cmu.edu/~15150/) - CMU's functional programming course taught in Standard ML.
- [Standard ML Basis Library](https://smlfamily.github.io/Basis/) - Reference documentation for the standard Basis Library.
- [Learn X in Y minutes: Standard ML](https://learnxinyminutes.com/docs/standard-ml/) - A whirlwind syntax tour for programmers coming from other languages.

## Tooling (community)

Build tools, package managers, formatters and language servers outside this ecosystem.

- [smlpkg](https://github.com/diku-dk/smlpkg) - A generic package manager for SML using Git/GitHub package paths; the layout the sjqtentacles libraries vendor against.
- [Millet](https://github.com/azdavis/millet) - A language server and VS Code extension for Standard ML.
- [smlfmt](https://github.com/shwestrick/smlfmt) - A custom parser and pretty-printer / formatter for SML source.
- [SML/NJ Compilation Manager (CM)](https://www.smlnj.org/doc/CM/) - SML/NJ's dependency-tracking build system.
- [ML Basis system (MLton)](http://mlton.org/MLBasis) - MLton's `.mlb` system for programming in the large.

## Editor support

Syntax highlighting and IDE integration.

- [VS Code SML extensions](https://marketplace.visualstudio.com/search?term=standard%20ml&target=VSCode) - Syntax highlighting and (via Millet) language-server features for Standard ML in VS Code.
- [sml-mode (Emacs)](https://elpa.nongnu.org/nongnu/sml-mode.html) - The long-standing Emacs major mode for editing SML.
- [Vim/Neovim SML support](https://github.com/jez/vim-better-sml) - Improved Standard ML editing for Vim, including Merlin-style features.

## Other lists & indexes

Related curated lists and package indexes.

- [awesome-fp (functional programming)](https://github.com/lucasviola/awesome-functional-programming) - A broad list of functional-programming resources across languages.

## sjqtentacles ecosystem

The [sjqtentacles](https://github.com/sjqtentacles) Standard ML ecosystem: 336 libraries.

### Developer tooling (SML self-tooling)

The cluster of tools that operate on Standard ML itself: a frontend (lexer/parser/AST), formatter, doc generator, language server, linter, type elaborator, package/build tool, test frameworks and benchmarking. 19 libraries.

- [sml-bench](https://github.com/sjqtentacles/sml-bench) - A deterministic, count-based micro-benchmark harness in pure Standard ML: measures operation counts (not wall-clock time) so results are exactly reproducible (MLton + Poly/ML).
- [sml-check](https://github.com/sjqtentacles/sml-check) - Pure Standard ML property-based testing with rose-tree shrinking (MLton + Poly/ML, deterministic seeds).
- [sml-doc](https://github.com/sjqtentacles/sml-doc) - A pure Standard ML documentation generator emitting static HTML/Markdown.
- [sml-editorcore](https://github.com/sjqtentacles/sml-editorcore) - Text-editor core in pure Standard ML: piece-table buffer, undo/redo history, Unicode-aware cursor, stable marks (MLton + Poly/ML).
- [sml-elab](https://github.com/sjqtentacles/sml-elab) - Pure Standard ML type elaborator: Hindley-Milner Algorithm W over the positioned sml-mlast AST, with principal types, row-polymorphic records, and spanned diagnostics. Byte-identical under MLton and Poly/ML.
- [sml-fmt](https://github.com/sjqtentacles/sml-fmt) - A pure Standard ML, deterministic and idempotent source code formatter.
- [sml-hm](https://github.com/sjqtentacles/sml-hm) - Hindley-Milner type inference (Algorithm W) for a mini-ML in pure Standard ML, with let-polymorphism and an ofLambda bridge to the vendored sml-lambda. Dual-compiler MLton + Poly/ML.
- [sml-lineedit](https://github.com/sjqtentacles/sml-lineedit) - A single-keystroke line-editing step function for Standard ML.
- [sml-lint](https://github.com/sjqtentacles/sml-lint) - Pure, deterministic static linter for Standard ML over the positioned sml-mlast AST: unused/shadow/dead-open/non-exhaustive/redundant-parens/naming rules. MLton + Poly/ML, byte-identical.
- [sml-lsp](https://github.com/sjqtentacles/sml-lsp) - A pure Standard ML language server (LSP over JSON-RPC) for Standard ML.
- [sml-mlast](https://github.com/sjqtentacles/sml-mlast) - A pure Standard ML lexer, parser, AST and pretty-printer for Standard ML '97.
- [sml-pkg](https://github.com/sjqtentacles/sml-pkg) - Pure Standard ML package-manifest resolver + lockfile + .mlb generator (smlpkg-compatible), with a thin Git/mlton build driver. Byte-identical under MLton and Poly/ML.
- [sml-pretty](https://github.com/sjqtentacles/sml-pretty) - A Wadler/Leijen pretty-printer combinator library in pure Standard ML (group/nest/line, width-aware layout).
- [sml-readline](https://github.com/sjqtentacles/sml-readline) - Pure Standard ML line-editor state machine: key model, ANSI decoder, history, kill-ring, completion hook (MLton + Poly/ML).
- [sml-resolver](https://github.com/sjqtentacles/sml-resolver) - A SAT-backed package dependency resolver using semver ranges and DPLL for Standard ML.
- [sml-semver](https://github.com/sjqtentacles/sml-semver) - Pure Standard ML SemVer 2.0.0 parser, comparison, and range matching (MLton + Poly/ML, deterministic).
- [sml-stlc](https://github.com/sjqtentacles/sml-stlc) - Simply-typed lambda calculus with Curry-Howard bridge to natural deduction, in pure SML.
- [sml-test](https://github.com/sjqtentacles/sml-test) - A Standard ML test framework with property-based testing, QuickCheck-style generators, forAll, and shrinking.
- [sml-tls-tool](https://github.com/sjqtentacles/sml-tls-tool) - Conformance and fuzzing harnesses for sml-tls: BoGo shim, tlsfuzzer driver, OpenSSL differential, AFL persistent-mode fuzzers. Impure, quarantined.

### Cryptography & security

Hashes, ciphers, AEAD, public-key crypto, key derivation, TLS, X.509, and related security primitives. 30 libraries.

- [sml-aead](https://github.com/sjqtentacles/sml-aead) - Unified AEAD facade (ChaCha20-Poly1305 + AES-128/256-GCM) in pure Standard ML, with byte-exact RFC 8439 / NIST GCM vectors. Dual-compiler (MLton + Poly/ML).
- [sml-aes](https://github.com/sjqtentacles/sml-aes) - AES block cipher with ECB, CBC, CTR, and GCM modes in pure Standard ML (FIPS 197).
- [sml-asn1](https://github.com/sjqtentacles/sml-asn1) - ASN.1 DER encoder/decoder for Standard ML (INTEGER/SEQUENCE/OID/… via arbitrary-precision integers). Pure, dual-compiler.
- [sml-bigint](https://github.com/sjqtentacles/sml-bigint) - Arbitrary-precision signed integers for Standard ML: Karatsuba multiply, divMod, gcd, modpow, Miller-Rabin. Pure, dual-compiler.
- [sml-blake3](https://github.com/sjqtentacles/sml-blake3) - BLAKE3 cryptographic hash function in pure Standard ML.
- [sml-chacha20](https://github.com/sjqtentacles/sml-chacha20) - ChaCha20-Poly1305 and XChaCha20-Poly1305 AEAD in pure Standard ML (RFC 8439).
- [sml-codec](https://github.com/sjqtentacles/sml-codec) - Binary codecs for Standard ML: Base64/Base16 (RFC 4648), SHA-1 (RFC 3174), SHA-256 (RFC 6234), CRC-32. Verified against RFC vectors. Pure, dual-compiler.
- [sml-cookie](https://github.com/sjqtentacles/sml-cookie) - RFC 6265 Cookie/Set-Cookie parse+build for Standard ML (Path, Domain, Max-Age, Expires, Secure, HttpOnly, SameSite) plus HMAC-signed cookies. Pure, dual-compiler.
- [sml-cose](https://github.com/sjqtentacles/sml-cose) - COSE (RFC 8152 / RFC 9052) CBOR message structures in pure Standard ML (MLton + Poly/ML).
- [sml-crypto](https://github.com/sjqtentacles/sml-crypto) - HMAC-SHA256 (RFC 4231), constant-time compare, and signed tokens for Standard ML. Verified against RFC vectors. Pure, dual-compiler.
- [sml-ed25519](https://github.com/sjqtentacles/sml-ed25519) - Ed25519 digital signatures over Edwards25519 in pure Standard ML (RFC 8032).
- [sml-html](https://github.com/sjqtentacles/sml-html) - HTML AST with safe-by-default, context-aware escaping for Standard ML. XSS holes are opt-in and greppable. Pure, dual-compiler (MLton + Poly/ML).
- [sml-jwt](https://github.com/sjqtentacles/sml-jwt) - A Standard ML library for JSON Web Tokens (JWS) with HMAC-SHA256 (HS256) signing and verification.
- [sml-kdf](https://github.com/sjqtentacles/sml-kdf) - Key-derivation functions in pure Standard ML: HKDF (RFC 5869) + scrypt (RFC 7914), with byte-exact RFC vectors. Dual-compiler (MLton + Poly/ML).
- [sml-merkle](https://github.com/sjqtentacles/sml-merkle) - Merkle tree construction, root computation, and inclusion proofs in pure Standard ML.
- [sml-oauth](https://github.com/sjqtentacles/sml-oauth) - OAuth 2.0 + PKCE (RFC 6749 / RFC 7636) as a pure state machine in Standard ML (MLton + Poly/ML).
- [sml-p256](https://github.com/sjqtentacles/sml-p256) - NIST P-256 (secp256r1) ECDH key agreement and ECDSA signature verification in pure Standard ML. Built on sml-bigint, sml-asn1, sml-codec. Pure, dual-compiler.
- [sml-pem](https://github.com/sjqtentacles/sml-pem) - Pure Standard ML PEM encode/decode (RFC 7468) over Base64 (MLton + Poly/ML).
- [sml-ripemd160](https://github.com/sjqtentacles/sml-ripemd160) - RIPEMD-160 cryptographic hash for Standard ML (Bitcoin hash160), verified against the official test vectors. Pure, dual-compiler.
- [sml-rsa](https://github.com/sjqtentacles/sml-rsa) - Pure Standard ML RSA: keygen, PKCS#1 v1.5 / OAEP / PSS, DER/PEM keys (MLton + Poly/ML).
- [sml-sanitize](https://github.com/sjqtentacles/sml-sanitize) - Allowlist HTML sanitizer in pure Standard ML (MLton + Poly/ML), built on sml-html.
- [sml-secp256k1](https://github.com/sjqtentacles/sml-secp256k1) - ECDSA and Schnorr (BIP-340) signatures over secp256k1 in pure Standard ML.
- [sml-session](https://github.com/sjqtentacles/sml-session) - Pure session handling for Standard ML: one string->string model with in-memory and stateless HMAC-signed-cookie backends. Pure, dual-compiler.
- [sml-sha3](https://github.com/sjqtentacles/sml-sha3) - Keccak-f\[1600\] sponge, SHA3-224/256/384/512, SHAKE128/SHAKE256 XOF, and KMAC in pure Standard ML.
- [sml-shamir](https://github.com/sjqtentacles/sml-shamir) - Pure Standard ML Shamir Secret Sharing over GF(256) (MLton + Poly/ML).
- [sml-tls](https://github.com/sjqtentacles/sml-tls) - TLS 1.3 (RFC 8446) sans-IO state machine in pure Standard ML, verified against RFC 8448 vectors. Experimental, not for production security.
- [sml-totp](https://github.com/sjqtentacles/sml-totp) - Pure Standard ML HOTP/TOTP (RFC 4226 / RFC 6238), HMAC-SHA1/256/512 (MLton + Poly/ML).
- [sml-trie](https://github.com/sjqtentacles/sml-trie) - Merkle Patricia Trie for key-value storage with cryptographic root hashing in pure Standard ML.
- [sml-x25519](https://github.com/sjqtentacles/sml-x25519) - Curve25519 Diffie-Hellman key exchange (RFC 7748) in pure Standard ML.
- [sml-x509](https://github.com/sjqtentacles/sml-x509) - Pure Standard ML X.509 certificate parser and RSA signature verifier (MLton + Poly/ML, deterministic).

### Blockchain & cryptocurrency

Bitcoin, Ethereum and related ledger/encoding primitives. 7 libraries.

- [sml-base58](https://github.com/sjqtentacles/sml-base58) - Base58 and Base58Check codec for Standard ML (Bitcoin alphabet, double-SHA256 checksum). Pure, dual-compiler.
- [sml-bech32](https://github.com/sjqtentacles/sml-bech32) - Bech32 and Bech32m encoding with SegwitAddr support in pure Standard ML (BIP-173/350).
- [sml-bip32](https://github.com/sjqtentacles/sml-bip32) - Pure Standard ML BIP-32 hierarchical deterministic wallets (private-tree CKDpriv + neuter, P2PKH) (MLton + Poly/ML).
- [sml-bip39](https://github.com/sjqtentacles/sml-bip39) - Pure Standard ML BIP-39 mnemonic seed phrases (PBKDF2-HMAC-SHA512) (MLton + Poly/ML).
- [sml-rlp](https://github.com/sjqtentacles/sml-rlp) - Recursive Length Prefix (RLP) encoder/decoder for Ethereum in pure Standard ML.
- [sml-script](https://github.com/sjqtentacles/sml-script) - Bitcoin Script stack machine interpreter (subset) in pure Standard ML.
- [sml-utxo](https://github.com/sjqtentacles/sml-utxo) - Bitcoin-style Unspent Transaction Output (UTXO) model in pure Standard ML.

### Media containers & codecs

Image, audio and video container formats and codec parsers: JPEG baseline decoding, FLAC and Ogg framing, RIFF chunks, ISO BMFF (MP4) box scanning, and Matroska/EBML header detection. 6 libraries.

- [sml-flac](https://github.com/sjqtentacles/sml-flac) - A FLAC metadata and frame-header parser for Standard ML (STREAMINFO + frame parsing; LPC residual decoding is a documented stub).
- [sml-jpeg](https://github.com/sjqtentacles/sml-jpeg) - JPEG header parsing (SOI detection and Start-of-Frame geometry) for Standard ML.
- [sml-mkv](https://github.com/sjqtentacles/sml-mkv) - Matroska / WebM (EBML) magic-number / header recognition for Standard ML.
- [sml-mp4](https://github.com/sjqtentacles/sml-mp4) - A flat ISO Base Media File Format (MP4/MOV) top-level box scanner (no nested children) for Standard ML.
- [sml-ogg](https://github.com/sjqtentacles/sml-ogg) - Ogg container page segmentation with lacing-table parsing for Standard ML.
- [sml-riff](https://github.com/sjqtentacles/sml-riff) - A RIFF container chunk reader/writer (WAV, AVI, WebP) for Standard ML.

### Encoding, serialization & compression

Wire formats, text/binary codecs, structured-data parsers, and compression algorithms. 31 libraries.

- [sml-base32](https://github.com/sjqtentacles/sml-base32) - Pure Standard ML Base32 codec: RFC 4648, base32hex, Crockford, z-base-32 (MLton + Poly/ML).
- [sml-bencode](https://github.com/sjqtentacles/sml-bencode) - BitTorrent bencode encoder/decoder in pure Standard ML with canonical dictionary ordering. Deterministic, MLton + Poly/ML.
- [sml-cbor](https://github.com/sjqtentacles/sml-cbor) - CBOR (Concise Binary Object Representation) encoder/decoder in pure Standard ML (RFC 8949).
- [sml-css](https://github.com/sjqtentacles/sml-css) - Typed CSS model in pure Standard ML: selector/declaration/stylesheet algebra with a deterministic serializer and a round-tripping parser. Dual-compiler (MLton + Poly/ML), byte-identical, zero deps.
- [sml-csv](https://github.com/sjqtentacles/sml-csv) - A Standard ML RFC 4180 CSV/TSV parser and writer with full quoting and escaping.
- [sml-deflate](https://github.com/sjqtentacles/sml-deflate) - RFC 1951 DEFLATE inflate + RFC 1950/1952 zlib/gzip wrappers for Standard ML. Verified against known compressed vectors. Pure, dual-compiler.
- [sml-gemini](https://github.com/sjqtentacles/sml-gemini) - Pure Standard ML codec for the Gemini protocol and gemtext markup — dependency-free, MLton + Poly/ML.
- [sml-gif](https://github.com/sjqtentacles/sml-gif) - Pure Standard ML animated GIF encoder (LZW + median-cut palette) (MLton + Poly/ML).
- [sml-gzip](https://github.com/sjqtentacles/sml-gzip) - A Standard ML gzip (RFC 1952) container codec over DEFLATE/INFLATE with CRC32 verification.
- [sml-hex](https://github.com/sjqtentacles/sml-hex) - Portable hexadecimal encode/decode for Standard ML (MLton + Poly/ML): byte and string entry points, strict decoding, mixed-case tolerant.
- [sml-inflate](https://github.com/sjqtentacles/sml-inflate) - DEFLATE/zlib/gzip decompression for Standard ML (MLton + Poly/ML): RFC 1950/1951/1952, CRC-32 and Adler-32, fixed and dynamic Huffman. Pure, FFI-free.
- [sml-json](https://github.com/sjqtentacles/sml-json) - Self-contained JSON parser + serializer for Standard ML, built on (vendored) sml-parsec.
- [sml-jsonpath](https://github.com/sjqtentacles/sml-jsonpath) - Pure Standard ML JSONPath query engine over sml-json (MLton + Poly/ML).
- [sml-lz4](https://github.com/sjqtentacles/sml-lz4) - Pure Standard ML LZ4 block-format compressor and decompressor (zero dependencies, MLton + Poly/ML).
- [sml-msgpack](https://github.com/sjqtentacles/sml-msgpack) - MessagePack binary serialization (spec v2.0) in pure Standard ML.
- [sml-openapi](https://github.com/sjqtentacles/sml-openapi) - Typed OpenAPI 3.0 model with YAML + JSON parsing and serialization in pure Standard ML (MLton + Poly/ML).
- [sml-pdf](https://github.com/sjqtentacles/sml-pdf) - Pure Standard ML PDF generator: page tree, vector graphics, Core-14 base fonts, FlateDecode - no font embedding.
- [sml-protobuf](https://github.com/sjqtentacles/sml-protobuf) - Protocol Buffers wire-format codec for Standard ML (varint, zigzag, length-delimited, fixed32/64). Pure, dual-compiler.
- [sml-qrcode](https://github.com/sjqtentacles/sml-qrcode) - Pure Standard ML QR code generator (Reed-Solomon GF(256) + masking) (MLton + Poly/ML).
- [sml-schema](https://github.com/sjqtentacles/sml-schema) - JSON Schema (draft 2020-12) parser and validator in pure Standard ML, built on sml-json (MLton + Poly/ML).
- [sml-sexp](https://github.com/sjqtentacles/sml-sexp) - S-expression reader/writer (Lisp/Scheme atoms, lists, quote forms; line + block comments) for Standard ML, built on sml-parsec. Pure, dual-compiler.
- [sml-sqlite](https://github.com/sjqtentacles/sml-sqlite) - Pure Standard ML reader for the SQLite database file format: B-tree pages, native varint, record codec - zero dependencies.
- [sml-sse](https://github.com/sjqtentacles/sml-sse) - Pure Standard ML codec for Server-Sent Events (text/event-stream) — dependency-free, MLton + Poly/ML.
- [sml-suffixarray](https://github.com/sjqtentacles/sml-suffixarray) - Suffix arrays, Kasai LCP, Burrows-Wheeler transform/inverse, and SA substring search in pure Standard ML (MLton + Poly/ML).
- [sml-tar](https://github.com/sjqtentacles/sml-tar) - Pure Standard ML POSIX ustar tar archive read/write (MLton + Poly/ML).
- [sml-toml](https://github.com/sjqtentacles/sml-toml) - A Standard ML TOML parser and serializer (subset of v1.0.0) built on parser combinators.
- [sml-varint](https://github.com/sjqtentacles/sml-varint) - Pure Standard ML variable-length integer codec: LEB128, zigzag, protobuf varints (MLton + Poly/ML, byte-exact).
- [sml-xml](https://github.com/sjqtentacles/sml-xml) - Namespaced XML parser, DOM, and serializer for Standard ML (entities, CDATA, comments). Pure, dual-compiler.
- [sml-yaml](https://github.com/sjqtentacles/sml-yaml) - Subset YAML 1.2 parser (block + flow, multi-doc) in pure Standard ML.
- [sml-zip](https://github.com/sjqtentacles/sml-zip) - Pure Standard ML PK ZIP archive read/write (store + deflate, CRC-32, central directory) (MLton + Poly/ML).
- [sml-zstd](https://github.com/sjqtentacles/sml-zstd) - Pure Standard ML Zstandard (RFC 8878) decompressor plus a raw-block compressor - zero dependencies.

### Web, networking & protocols

HTTP and friends, web framework pieces, sockets, and internet protocols. 23 libraries.

- [sml-dns](https://github.com/sjqtentacles/sml-dns) - Pure Standard ML DNS message wire codec with name compression, RFC 1035 (MLton + Poly/ML).
- [sml-dns-resolve](https://github.com/sjqtentacles/sml-dns-resolve) - DNS stub resolver in pure Standard ML: TTL-aware LRU cache, CNAME chains, typed answers, built on sml-dns (MLton + Poly/ML).
- [sml-email](https://github.com/sjqtentacles/sml-email) - A MIME multipart email parser and serialiser for Standard ML.
- [sml-feed](https://github.com/sjqtentacles/sml-feed) - Unified RSS 2.0 + Atom 1.0 feed parser and generator in pure Standard ML (MLton + Poly/ML).
- [sml-forms](https://github.com/sjqtentacles/sml-forms) - Decode form/query/JSON bodies into typed values for Standard ML via a validation applicative that accumulates errors. Pure, dual-compiler.
- [sml-git](https://github.com/sjqtentacles/sml-git) - Pure Standard ML Git plumbing: object, packfile, index and ref formats (MLton + Poly/ML, deterministic).
- [sml-http](https://github.com/sjqtentacles/sml-http) - RFC 9110/9112 HTTP/1.1 message model for Standard ML: request/response records, case-insensitive headers, parser, chunked + Content-Length framing, CLI. Pure, dual-compiler.
- [sml-http2](https://github.com/sjqtentacles/sml-http2) - HTTP/2 framing + HPACK header compression in pure Standard ML, verified against RFC 7541 vectors (MLton + Poly/ML).
- [sml-httpc](https://github.com/sjqtentacles/sml-httpc) - Pure sans-IO HTTP/1.1 client state machine in Standard ML (request builder + incremental response/chunked decoder + redirect logic). Dual-compiler (MLton + Poly/ML).
- [sml-httpc-tool](https://github.com/sjqtentacles/sml-httpc-tool) - Impure TCP socket driver + CLI for the pure sml-httpc HTTP/1.1 client. Quarantined IO tool (not dual-compiler-guaranteed); plain HTTP only.
- [sml-ipaddr](https://github.com/sjqtentacles/sml-ipaddr) - IPv4/IPv6 address parsing, CIDR arithmetic, and RFC 5952 canonical formatting in pure Standard ML (MLton + Poly/ML).
- [sml-middleware](https://github.com/sjqtentacles/sml-middleware) - Composable handler->handler middleware for Standard ML: compose, error catching, body limits, logging, headers, in-memory static files (glob). Pure, dual-compiler.
- [sml-mime](https://github.com/sjqtentacles/sml-mime) - MIME for Standard ML: media-type parse/format (RFC 9110), multipart/form-data splitter+builder (RFC 7578), extension->MIME table. Pure, dual-compiler.
- [sml-mqtt](https://github.com/sjqtentacles/sml-mqtt) - MQTT 3.1.1/5.0 packet codec + pure client state machine in pure Standard ML (MLton + Poly/ML), zero dependencies.
- [sml-negotiate](https://github.com/sjqtentacles/sml-negotiate) - RFC 9110 proactive content negotiation for Standard ML: Accept / Accept-Encoding / Accept-Language parsing + q-value best-match. Pure, dual-compiler.
- [sml-redis](https://github.com/sjqtentacles/sml-redis) - Pure Standard ML RESP protocol codec and Redis command builders (MLton + Poly/ML).
- [sml-robots](https://github.com/sjqtentacles/sml-robots) - Pure Standard ML robots.txt parser and matcher (RFC 9309) — dependency-free, MLton + Poly/ML.
- [sml-router](https://github.com/sjqtentacles/sml-router) - Pure HTTP router for Standard ML: path patterns with :params and *wildcards, method dispatch, request->response handlers. Pure, dual-compiler.
- [sml-serve](https://github.com/sjqtentacles/sml-serve) - Design doc (not a buildable library) for the MLton-only socket adapter that drives an sml-web app via sml-async: the one impure edge of the pure-SML web stack.
- [sml-smtp](https://github.com/sjqtentacles/sml-smtp) - SMTP (RFC 5321) codec, RFC 5322 message assembly, and a sans-IO client state machine in pure Standard ML (MLton + Poly/ML).
- [sml-uri](https://github.com/sjqtentacles/sml-uri) - RFC 3986 URI + x-www-form-urlencoded for Standard ML: percent codec, parse/toString, reference resolution, query handling, CLI. Pure, dual-compiler.
- [sml-web](https://github.com/sjqtentacles/sml-web) - Umbrella of the pure-SML web stack: one request->response app wiring router + middleware + sessions + negotiation. Pure, deterministic, dual-compiler.
- [sml-ws](https://github.com/sjqtentacles/sml-ws) - RFC 6455 WebSockets for Standard ML: Sec-WebSocket-Accept handshake, frame encode/decode, fragmentation reassembly. Verified against RFC vectors. Pure, dual-compiler.

### Parsing & languages

Parsers, interpreters, term rewriting, logic programming and small language runtimes. 20 libraries.

- [sml-free](https://github.com/sjqtentacles/sml-free) - Free monad and interpreter pattern over a key/value DSL in pure Standard ML.
- [sml-glob](https://github.com/sjqtentacles/sml-glob) - Shell-style glob matching for Standard ML (MLton + Poly/ML): *, ?, \[classes\], ranges, negation, escapes, case-insensitive. Pure backtracking matcher.
- [sml-graphql](https://github.com/sjqtentacles/sml-graphql) - GraphQL executable-document parser, AST and deterministic pretty-printer in pure Standard ML (MLton + Poly/ML).
- [sml-lambda](https://github.com/sjqtentacles/sml-lambda) - Untyped + simply-typed lambda calculus: parser, capture-avoiding substitution, normal-order reduction, STLC typechecker, in pure Standard ML (MLton + Poly/ML).
- [sml-lisp](https://github.com/sjqtentacles/sml-lisp) - A small functional Scheme interpreter in Standard ML (MLton + Poly/ML): closures, IntInf bignums, proper tail calls.
- [sml-markdown](https://github.com/sjqtentacles/sml-markdown) - CommonMark-subset Markdown parser in pure Standard ML, rendering to an sml-html node tree (MLton + Poly/ML).
- [sml-minikanren](https://github.com/sjqtentacles/sml-minikanren) - Pure Standard ML miniKanren: relational logic programming (==, =/=, conde, fresh, run/reify) over fair streams (MLton + Poly/ML).
- [sml-packrat](https://github.com/sjqtentacles/sml-packrat) - Memoizing PEG (packrat) parser for Standard ML (MLton + Poly/ML): ordered choice, & / ! predicates, linear-time memoization.
- [sml-parsec](https://github.com/sjqtentacles/sml-parsec) - Parser combinators for Standard ML (MLton + Poly/ML), with position tracking and precise error reporting.
- [sml-queryparse](https://github.com/sjqtentacles/sml-queryparse) - A full-text search Boolean query parser producing an AST for Standard ML.
- [sml-rederiv](https://github.com/sjqtentacles/sml-rederiv) - A Standard ML regular-expression engine using Brzozowski derivatives, with search, replace, and bounded quantifiers.
- [sml-regex](https://github.com/sjqtentacles/sml-regex) - A linear-time regular expression engine (Thompson NFA + Pike VM) with capture groups for Standard ML.
- [sml-rewrite](https://github.com/sjqtentacles/sml-rewrite) - First-order term rewriting in pure Standard ML: unification, matching, LPO, critical pairs, and Knuth-Bendix completion (dual-compiler MLton + Poly/ML).
- [sml-sh](https://github.com/sjqtentacles/sml-sh) - A tiny POSIX-ish shell line parser producing a command AST for Standard ML.
- [sml-shglob](https://github.com/sjqtentacles/sml-shglob) - Shell glob matching and brace expansion for Standard ML.
- [sml-ssg](https://github.com/sjqtentacles/sml-ssg) - Pure Standard ML static-site-generator core: frontmatter + markdown + template -> HTML (MLton + Poly/ML).
- [sml-template](https://github.com/sjqtentacles/sml-template) - Logic-light Mustache/Handlebars-style templating engine in pure Standard ML (MLton + Poly/ML), with HTML escaping.
- [sml-vdom](https://github.com/sjqtentacles/sml-vdom) - Virtual DOM in pure Standard ML: diff two sml-html trees into a minimal patch list with a round-tripping apply oracle. Dual-compiler (MLton + Poly/ML), byte-identical, deterministic.
- [sml-vm](https://github.com/sjqtentacles/sml-vm) - A small stack-based bytecode VM, label-resolving assembler, and disassembler in pure Standard ML (MLton + Poly/ML).
- [sml-wasm](https://github.com/sjqtentacles/sml-wasm) - Pure Standard ML WebAssembly toolkit: binary .wasm decoder, .wat text parser, and a stack-machine interpreter.

### Information retrieval & NLP

Full-text search, ranking, tokenization, language models and bioinformatics sequence tooling. 7 libraries.

- [sml-bio](https://github.com/sjqtentacles/sml-bio) - Bioinformatics toolkit in pure Standard ML: FASTA/FASTQ parsing, reverse complement, GC content, Needleman-Wunsch & Smith-Waterman alignment. MLton + Poly/ML.
- [sml-bm25](https://github.com/sjqtentacles/sml-bm25) - Okapi BM25 / TF-IDF document ranking in pure Standard ML, built on an inverted index. Deterministic, MLton + Poly/ML.
- [sml-bpe](https://github.com/sjqtentacles/sml-bpe) - Byte-pair encoding (BPE) subword tokenizer in pure Standard ML: train, encode, decode. Deterministic, MLton + Poly/ML.
- [sml-fts](https://github.com/sjqtentacles/sml-fts) - A small full-text search index with Porter stemming and an inverted index for Standard ML.
- [sml-invertedindex](https://github.com/sjqtentacles/sml-invertedindex) - Inverted index for full-text search in pure Standard ML: boolean queries (AND/OR/NOT) and positional phrase matching. Deterministic, MLton + Poly/ML.
- [sml-ngram](https://github.com/sjqtentacles/sml-ngram) - N-gram language models in pure Standard ML with add-k and interpolated backoff smoothing; perplexity. Deterministic, MLton + Poly/ML.
- [sml-stemmer](https://github.com/sjqtentacles/sml-stemmer) - English word stemming (Porter and Snowball English) for Standard ML.

### Formal methods & logic

Theorem proving, model checking, SAT/SMT solving and decision diagrams. 8 libraries.

- [sml-argumentation](https://github.com/sjqtentacles/sml-argumentation) - Dung abstract argumentation frameworks: labelling and SAT engines in pure SML.
- [sml-bdd](https://github.com/sjqtentacles/sml-bdd) - Reduced ordered binary decision diagrams (ROBDDs) with a hash-consing manager, in pure Standard ML (MLton + Poly/ML).
- [sml-collision](https://github.com/sjqtentacles/sml-collision) - 2D AABB, circle, and SAT convex polygon collision detection in pure Standard ML.
- [sml-logic](https://github.com/sjqtentacles/sml-logic) - Propositional logic toolkit: parser, truth tables, tautology/SAT/equivalence, NNF/CNF/DNF, in pure Standard ML (MLton + Poly/ML).
- [sml-modelcheck](https://github.com/sjqtentacles/sml-modelcheck) - Symbolic CTL model checking over finite Kripke structures in pure Standard ML, using the vendored sml-bdd ROBDD library. Dual-compiler MLton + Poly/ML.
- [sml-proof](https://github.com/sjqtentacles/sml-proof) - Natural-deduction proof checker for classical propositional logic in pure Standard ML, built on the vendored sml-logic formula type. Dual-compiler MLton + Poly/ML.
- [sml-sat](https://github.com/sjqtentacles/sml-sat) - DPLL SAT solver with a DIMACS CNF parser, in pure Standard ML (MLton + Poly/ML).
- [sml-smt](https://github.com/sjqtentacles/sml-smt) - Lazy DPLL(T) SMT solver in pure Standard ML over the vendored sml-sat DPLL core: EUF (congruence closure) + LRA (Fourier-Motzkin). Dual-compiler MLton + Poly/ML.

### Math, numeric & scientific

Arbitrary precision, linear algebra, statistics, signal processing, physics, astronomy and other numerics. 57 libraries.

- [sml-ad-rev](https://github.com/sjqtentacles/sml-ad-rev) - Forward-mode automatic differentiation for Standard ML.
- [sml-annealing](https://github.com/sjqtentacles/sml-annealing) - Generic simulated annealing optimizer in pure Standard ML with configurable cooling schedules (seeded PRNG). Deterministic, MLton + Poly/ML.
- [sml-astro](https://github.com/sjqtentacles/sml-astro) - Astronomy basics in pure Standard ML: Julian/Modified Julian dates, a Newton Kepler-equation orbit solver, and low-precision solar position (declination, equation of time). Deterministic, byte-identical on MLton and Poly/ML.
- [sml-autodiff](https://github.com/sjqtentacles/sml-autodiff) - Pure Standard ML automatic differentiation: forward (dual numbers) and reverse (tape) modes (MLton + Poly/ML, deterministic).
- [sml-bayesnet](https://github.com/sjqtentacles/sml-bayesnet) - Discrete Bayesian network inference via full enumeration for Standard ML.
- [sml-bigdecimal](https://github.com/sjqtentacles/sml-bigdecimal) - Arbitrary-precision decimal arithmetic for Standard ML (Java BigDecimal style), built on IntInf with explicit rounding modes. Portable, tested on MLton and Poly/ML.
- [sml-chem](https://github.com/sjqtentacles/sml-chem) - Chemistry toolkit in pure Standard ML: periodic table, formula parser, molar mass, and stoichiometric equation balancing. Deterministic on MLton and Poly/ML.
- [sml-cluster](https://github.com/sjqtentacles/sml-cluster) - Clustering in pure Standard ML: k-means (k-means++), DBSCAN, and hierarchical agglomerative clustering. Deterministic, byte-identical on MLton and Poly/ML.
- [sml-combinatorics](https://github.com/sjqtentacles/sml-combinatorics) - Combinatorial enumeration and exact counting in pure Standard ML: permutations, combinations, partitions, Gray codes, Catalan/Stirling numbers (IntInf). MLton + Poly/ML.
- [sml-complex](https://github.com/sjqtentacles/sml-complex) - Pure Standard ML complex numbers: arithmetic, exp/log/sqrt, powers, trig/hyperbolic and inverse functions, nth-roots, and polar form — deterministic across MLton and Poly/ML.
- [sml-constants](https://github.com/sjqtentacles/sml-constants) - CODATA fundamental physical constants as typed, dimensioned quantities in pure Standard ML, built on sml-units (MLton + Poly/ML).
- [sml-decisiontree](https://github.com/sjqtentacles/sml-decisiontree) - CART decision trees in pure Standard ML for classification and regression (Gini, entropy, variance). Deterministic, MLton + Poly/ML.
- [sml-distrib](https://github.com/sjqtentacles/sml-distrib) - Probability distributions (pdf, cdf, and pure functional sampling via SplitMix64) for Standard ML.
- [sml-dsp](https://github.com/sjqtentacles/sml-dsp) - Frequency-domain DSP in pure Standard ML: windows, RBJ biquads, windowed-sinc FIR, IIR, FFT convolution, STFT/ISTFT (MLton + Poly/ML).
- [sml-fft](https://github.com/sjqtentacles/sml-fft) - Fast Fourier Transform (FFT/IFFT, real-FFT, FFT convolution) for Standard ML. Radix-2 + Bluestein. Pure, dual-compiler.
- [sml-ga](https://github.com/sjqtentacles/sml-ga) - Generic genetic algorithm optimizer in pure Standard ML: tournament selection, elitism, crossover, mutation (seeded PRNG). MLton + Poly/ML.
- [sml-geo](https://github.com/sjqtentacles/sml-geo) - GeoJSON (RFC 7946) typed geometry model with parser, serializer, and bbox in pure Standard ML (MLton + Poly/ML).
- [sml-geodesy](https://github.com/sjqtentacles/sml-geodesy) - WGS-84 geodesy in pure Standard ML: haversine, Vincenty geodesics, and UTM projection (MLton + Poly/ML).
- [sml-glm](https://github.com/sjqtentacles/sml-glm) - Graphics linear algebra for Standard ML (MLton + Poly/ML): vec2/3/4, mat2/3/4, quaternions, transforms, projections. Column-major, OpenGL conventions, pure (no FFI).
- [sml-gmm](https://github.com/sjqtentacles/sml-gmm) - Gaussian Mixture Model fitting via Expectation-Maximization for Standard ML.
- [sml-gp](https://github.com/sjqtentacles/sml-gp) - Gaussian-process regression with a squared-exponential (RBF) kernel for Standard ML.
- [sml-gpx](https://github.com/sjqtentacles/sml-gpx) - GPX waypoint reading/writing and great-circle distance for Standard ML.
- [sml-hmm](https://github.com/sjqtentacles/sml-hmm) - Hidden Markov Models in pure Standard ML: forward/backward, Viterbi, Baum-Welch. Built on a matrix library. MLton + Poly/ML.
- [sml-hungarian](https://github.com/sjqtentacles/sml-hungarian) - Assignment problem (Hungarian/Kuhn-Munkres) and Hopcroft-Karp bipartite matching in pure Standard ML, integer arithmetic (MLton + Poly/ML).
- [sml-itersolve](https://github.com/sjqtentacles/sml-itersolve) - Iterative linear solvers (Conjugate Gradient) for sparse systems in Standard ML.
- [sml-kalman](https://github.com/sjqtentacles/sml-kalman) - Linear Kalman filter and recursive least squares in pure Standard ML, over the vendored sml-matrix. Dual-compiler (MLton & Poly/ML), deterministic.
- [sml-knn](https://github.com/sjqtentacles/sml-knn) - K-Nearest-Neighbors classification and regression in pure Standard ML, built on a k-d tree (majority vote / weighted averaging). MLton + Poly/ML.
- [sml-markov](https://github.com/sjqtentacles/sml-markov) - Discrete-time Markov chains in pure Standard ML: n-step distributions, stationary distribution, and seeded trajectory sampling. Deterministic on MLton and Poly/ML.
- [sml-matrix](https://github.com/sjqtentacles/sml-matrix) - A Standard ML dense linear algebra library: multiply, transpose, LU, determinant, solve, inverse, QR.
- [sml-mcmc](https://github.com/sjqtentacles/sml-mcmc) - MCMC samplers in pure Standard ML: Metropolis-Hastings and Gibbs with seeded PRNG (no ambient randomness). Deterministic, MLton + Poly/ML.
- [sml-money](https://github.com/sjqtentacles/sml-money) - Currency-aware money arithmetic in pure Standard ML on exact decimals: rounding modes and lossless allocation/splitting. MLton + Poly/ML.
- [sml-montecarlo](https://github.com/sjqtentacles/sml-montecarlo) - Seeded Monte-Carlo integration and estimation in pure Standard ML: 1-D/box integration, antithetic variates, and a pi estimate. Deterministic on MLton and Poly/ML.
- [sml-nbody](https://github.com/sjqtentacles/sml-nbody) - Barnes-Hut quadtree gravitational N-body in pure Standard ML: mass/center-of-mass quadtree, opening-angle force approximation, direct O(n^2) cross-check, symplectic leapfrog. Deterministic, byte-identical on MLton and Poly/ML.
- [sml-nn](https://github.com/sjqtentacles/sml-nn) - Neural networks in pure Standard ML on reverse-mode autodiff: dense layers, activations, MSE/CE, SGD/Adam.
- [sml-numbertheory](https://github.com/sjqtentacles/sml-numbertheory) - Pure Standard ML number theory: sieve, factorization, CRT, totient, Jacobi (MLton + Poly/ML).
- [sml-ode](https://github.com/sjqtentacles/sml-ode) - Pure Standard ML ODE integrators: Euler, RK4, adaptive RK45 (MLton + Poly/ML).
- [sml-optim](https://github.com/sjqtentacles/sml-optim) - Unconstrained numerical optimization (gradient descent and Nelder-Mead) for Standard ML.
- [sml-particle](https://github.com/sjqtentacles/sml-particle) - A Sequential Importance Resampling (SIR) particle filter for Standard ML.
- [sml-pca](https://github.com/sjqtentacles/sml-pca) - Principal Component Analysis in pure Standard ML via Jacobi eigen-decomposition: components, explained variance, transform. MLton + Poly/ML.
- [sml-pde](https://github.com/sjqtentacles/sml-pde) - Finite-difference PDE solvers (heat: FTCS + Crank-Nicolson; wave: leapfrog) on 1-D/2-D grids in pure Standard ML over sml-matrix. Dual-compiler (MLton & Poly/ML).
- [sml-physics](https://github.com/sjqtentacles/sml-physics) - 2D rigid-body and particle physics in pure Standard ML: symplectic integrators (Verlet/leapfrog/semi-implicit Euler), projectile closed forms, and a bouncing rigid-body world. Deterministic, byte-identical on MLton and Poly/ML.
- [sml-poly](https://github.com/sjqtentacles/sml-poly) - Univariate polynomials over an arbitrary ring for Standard ML, via a nesting Poly functor. Euclidean division and GCD over fields. Portable across MLton and Poly/ML.
- [sml-ppl](https://github.com/sjqtentacles/sml-ppl) - A probabilistic programming DSL with importance sampling and Metropolis-Hastings over a sampling stack for Standard ML.
- [sml-proj](https://github.com/sjqtentacles/sml-proj) - Cartographic projections (Web Mercator / EPSG:3857) for Standard ML.
- [sml-rational](https://github.com/sjqtentacles/sml-rational) - Exact rational-number arithmetic for Standard ML, built on IntInf. Portable (Basis-only), tested on MLton and Poly/ML.
- [sml-simplex](https://github.com/sjqtentacles/sml-simplex) - Linear and mixed-integer programming in pure Standard ML: two-phase simplex (Bland's rule) + branch-and-bound, dual-compiler (MLton & Poly/ML).
- [sml-sparse](https://github.com/sjqtentacles/sml-sparse) - Sparse matrix representations (COO and CSR) with sparse matrix-vector multiplication for Standard ML.
- [sml-spatialjoin](https://github.com/sjqtentacles/sml-spatialjoin) - Point-in-polygon testing and a point-to-polygon spatial join for Standard ML.
- [sml-specfun](https://github.com/sjqtentacles/sml-specfun) - Pure Standard ML special functions: gamma, beta, erf, incomplete gamma/beta (MLton + Poly/ML, deterministic).
- [sml-stats](https://github.com/sjqtentacles/sml-stats) - Pure Standard ML statistics: descriptive stats, distributions, regression, correlation, and hypothesis tests (t / chi-square / F) — MLton + Poly/ML.
- [sml-tensor](https://github.com/sjqtentacles/sml-tensor) - N-dimensional tensors in pure Standard ML: broadcasting, reshape/transpose, reductions, matmul, einsum.
- [sml-tiles](https://github.com/sjqtentacles/sml-tiles) - Slippy-map (Web Mercator) XYZ tile coordinate math for Standard ML.
- [sml-topojson](https://github.com/sjqtentacles/sml-topojson) - Minimal TopoJSON-style coordinate quantization for Standard ML.
- [sml-tvm](https://github.com/sjqtentacles/sml-tvm) - Time value of money in pure Standard ML: PV, FV, NPV, IRR, PMT, amortization schedules. Deterministic, MLton + Poly/ML.
- [sml-units](https://github.com/sjqtentacles/sml-units) - Runtime dimensional analysis for Standard ML: dimension-checked physical quantities over the SI base units. Portable across MLton and Poly/ML.
- [sml-wav](https://github.com/sjqtentacles/sml-wav) - Pure Standard ML WAV I/O and synth/DSP: oscillators, ADSR, biquad filters (MLton + Poly/ML).
- [sml-wkt](https://github.com/sjqtentacles/sml-wkt) - Well-Known Text (WKT) geometry parser & serializer in pure Standard ML, sharing the GeoJSON geometry AST. Deterministic, MLton + Poly/ML.

### Data structures

Trees, heaps, tries, maps, sets and other persistent/efficient containers. 21 libraries.

- [sml-bitset](https://github.com/sjqtentacles/sml-bitset) - Portable packed bit-set for Standard ML (MLton + Poly/ML): persistent set algebra, popcount, ascending iteration, fixed 32-bit chunks.
- [sml-bloom](https://github.com/sjqtentacles/sml-bloom) - Bloom filter with optimal sizing and SHA-256 hashing in pure Standard ML.
- [sml-btree](https://github.com/sjqtentacles/sml-btree) - Persistent in-memory B-tree (minimum degree t) in pure Standard ML (polymorphic keys, MLton + Poly/ML).
- [sml-buffer](https://github.com/sjqtentacles/sml-buffer) - Growable byte/char buffer with rope-style concat for Standard ML. Pure, deterministic, dual-compiler (MLton + Poly/ML).
- [sml-deque](https://github.com/sjqtentacles/sml-deque) - Purely functional double-ended queue for Standard ML (MLton + Poly/ML): banker's two-list deque, O(1) amortised both ends, persistent.
- [sml-fenwick](https://github.com/sjqtentacles/sml-fenwick) - Fenwick trees (BIT) and a lazy-propagation segment tree in pure Standard ML — persistent prefix/range sums, cumulative search, range-add/range-sum; dual-compiler (MLton + Poly/ML).
- [sml-fingertree](https://github.com/sjqtentacles/sml-fingertree) - Persistent 2-3 finger tree (sequence/deque) in pure Standard ML (MLton + Poly/ML).
- [sml-graph](https://github.com/sjqtentacles/sml-graph) - A Standard ML graph algorithms library: BFS, DFS, topological sort, SCC, MST, and max-flow.
- [sml-hamt](https://github.com/sjqtentacles/sml-hamt) - Persistent immutable hash map and vector (HAMT/CHAMP, 32-ary trie) for Standard ML, with structural sharing. Pure, dual-compiler.
- [sml-kdtree](https://github.com/sjqtentacles/sml-kdtree) - Balanced k-d trees in pure Standard ML: nearest-neighbour, k-NN, box, and radius queries over real coordinates. Deterministic, byte-identical on MLton and Poly/ML.
- [sml-lru](https://github.com/sjqtentacles/sml-lru) - Bounded LRU/LFU caches with optional TTL for Standard ML (functional, logical-clock based). Pure, dual-compiler.
- [sml-patricia](https://github.com/sjqtentacles/sml-patricia) - Compressed radix trie (Patricia tree) with longest-prefix match and prefix search in pure Standard ML. Pure, dual-compiler.
- [sml-pqueue](https://github.com/sjqtentacles/sml-pqueue) - Purely functional priority queue (pairing heap) for Standard ML (MLton + Poly/ML): functor over ORDERED, persistent, min/max-heap, O(1) merge.
- [sml-rbtree](https://github.com/sjqtentacles/sml-rbtree) - Persistent functional red-black maps and sets in pure Standard ML (polymorphic keys, MLton + Poly/ML).
- [sml-rope](https://github.com/sjqtentacles/sml-rope) - Persistent rope data structure with Fibonacci rebalancing in pure Standard ML.
- [sml-rtree](https://github.com/sjqtentacles/sml-rtree) - R-tree spatial index in pure Standard ML: quadratic-split insertion, window/containment/point-stab/nearest queries over rectangles. Deterministic, byte-identical on MLton and Poly/ML.
- [sml-skiplist](https://github.com/sjqtentacles/sml-skiplist) - Probabilistic skip list ordered map and set functor in pure Standard ML.
- [sml-timewheel](https://github.com/sjqtentacles/sml-timewheel) - Hierarchical timing wheel as a pure value in Standard ML: schedule, cancel, cascade, advance. Deterministic, MLton + Poly/ML.
- [sml-treap](https://github.com/sjqtentacles/sml-treap) - Persistent seeded treap (randomized balanced BST) in pure Standard ML: insert/delete/split/merge, ordered map, invariant validators — deterministic and byte-identical on MLton and Poly/ML.
- [sml-unionfind](https://github.com/sjqtentacles/sml-unionfind) - Disjoint-set / union-find (union by rank + path compression) for Standard ML. Pure, dual-compiler.
- [sml-zipper](https://github.com/sjqtentacles/sml-zipper) - Generic list and rose-tree zippers in pure Standard ML (MLton + Poly/ML).

### Algorithms

Graph, string, search and optimization algorithms not tied to a single data structure. 16 libraries.

- [sml-astar](https://github.com/sjqtentacles/sml-astar) - Generic A* and Dijkstra pathfinding with 2D grid support in pure Standard ML.
- [sml-bvh](https://github.com/sjqtentacles/sml-bvh) - Ray / axis-aligned bounding-box intersection (slab method) for Standard ML.
- [sml-clipper](https://github.com/sjqtentacles/sml-clipper) - 2D convex polygon Boolean intersection via Sutherland-Hodgman for Standard ML.
- [sml-csolver](https://github.com/sjqtentacles/sml-csolver) - Finite-domain constraint solver (CSP) in pure Standard ML: AC-3 arc consistency + backtracking. N-queens, Sudoku. MLton + Poly/ML.
- [sml-diff](https://github.com/sjqtentacles/sml-diff) - Myers O(ND) sequence diff for Standard ML: edit scripts, LCS, edit distance, and line-oriented text diffing. Portable across MLton and Poly/ML.
- [sml-dp](https://github.com/sjqtentacles/sml-dp) - Dynamic-programming toolkit in pure Standard ML: knapsack, LIS, coin change, matrix-chain, interval scheduling (MLton + Poly/ML).
- [sml-editdist](https://github.com/sjqtentacles/sml-editdist) - String distance metrics (Levenshtein, Damerau, Jaro, Jaro-Winkler) for fuzzy matching in Standard ML.
- [sml-fuzzy](https://github.com/sjqtentacles/sml-fuzzy) - Fuzzy string matching for Standard ML: Levenshtein/Damerau distance, similarity ranking, BK-tree, and Soundex. Pure, dual-compiler.
- [sml-geom2d](https://github.com/sjqtentacles/sml-geom2d) - Constructive 2D computational geometry in pure Standard ML: convex hull, Delaunay triangulation, polygon clipping, area/centroid — deterministic and byte-identical on MLton and Poly/ML.
- [sml-hull3](https://github.com/sjqtentacles/sml-hull3) - 3D convex hull computation producing a triangulated hull mesh for Standard ML.
- [sml-levauto](https://github.com/sjqtentacles/sml-levauto) - Levenshtein edit distance and dictionary fuzzy search for Standard ML.
- [sml-mincostflow](https://github.com/sjqtentacles/sml-mincostflow) - Minimum-cost maximum-flow in pure Standard ML via successive shortest augmenting paths (SPFA). Cost-aware extension over a graph library. MLton + Poly/ML.
- [sml-puzzles](https://github.com/sjqtentacles/sml-puzzles) - Classic puzzle solvers (N-Queens, Hanoi, Lights Out, Peg Solitaire) in pure Standard ML.
- [sml-stringalgo](https://github.com/sjqtentacles/sml-stringalgo) - Classic string matching & analysis in pure Standard ML: KMP, Z-function, Boyer-Moore, Rabin-Karp, Aho-Corasick, Manacher (MLton + Poly/ML).
- [sml-sudoku](https://github.com/sjqtentacles/sml-sudoku) - Deterministic 9x9 Sudoku constraint solver (candidate elimination + MRV backtracking) in pure Standard ML for MLton and Poly/ML.
- [sml-voronoi](https://github.com/sjqtentacles/sml-voronoi) - A 2D Voronoi diagram generator via half-plane intersection for Standard ML.

### Graphics, geometry & imaging

2D/3D math, rasterization, image codecs, fonts, color, layout and plotting. 16 libraries.

- [sml-camera](https://github.com/sjqtentacles/sml-camera) - Scene math for Standard ML (MLton + Poly/ML): transforms (TRS), camera view/projection, frustum culling, and ray/AABB/sphere/triangle intersection. Built on sml-glm, FFI-free.
- [sml-canvas2d](https://github.com/sjqtentacles/sml-canvas2d) - Pure-SML immediate 2D drawing-command model rendering one scene to both a raster image (sml-raster/sml-image) and SVG. Deterministic, byte-identical on MLton and Poly/ML.
- [sml-color](https://github.com/sjqtentacles/sml-color) - Color-space math for Standard ML (MLton + Poly/ML): sRGB/linear, HSL/HSV, RGBA8 packing, gamma, blending, interpolation. Deterministic and FFI-free.
- [sml-colorsci](https://github.com/sjqtentacles/sml-colorsci) - CIE colour-science extensions (XYZ, xyY, CIELUV, CIE94, Bradford adaptation, CCT) on top of sml-color, in pure Standard ML for MLton and Poly/ML.
- [sml-font](https://github.com/sjqtentacles/sml-font) - Pure Standard ML bitmap font (BDF) glyph rendering into sml-image (MLton + Poly/ML).
- [sml-image](https://github.com/sjqtentacles/sml-image) - Image codecs for Standard ML (MLton + Poly/ML): decode/encode PNM (PPM/PGM), BMP, TGA, and PNG (RGBA8). PNG built on vendored sml-inflate. Pure, FFI-free.
- [sml-layout](https://github.com/sjqtentacles/sml-layout) - Pure-SML constraint/flexbox box-layout solver: box tree + viewport -> resolved rects (Row/Column, flex-grow, basis, padding/margin/gap, justify/align), byte-identical on MLton and Poly/ML.
- [sml-mesh](https://github.com/sjqtentacles/sml-mesh) - An indexed face-list polygon mesh with face normals, the Euler characteristic, and Catmull-Clark subdivision for Standard ML.
- [sml-noise](https://github.com/sjqtentacles/sml-noise) - Procedural noise for Standard ML (MLton + Poly/ML): Perlin, simplex, value, and worley noise plus fbm/turbulence. Deterministic, seedable, pure (no FFI).
- [sml-obj](https://github.com/sjqtentacles/sml-obj) - Mesh parsers for Standard ML (MLton + Poly/ML): Wavefront OBJ/MTL and PLY (ASCII + binary little-endian). Triangulates faces, emits sml-glm vertex/index buffers. FFI-free.
- [sml-plot](https://github.com/sjqtentacles/sml-plot) - Pure Standard ML charting to PNG: line/bar/scatter/histogram with axes, ticks, and legend (MLton + Poly/ML).
- [sml-qoi](https://github.com/sjqtentacles/sml-qoi) - Pure Standard ML QOI (Quite OK Image) encoder/decoder (MLton + Poly/ML).
- [sml-raster](https://github.com/sjqtentacles/sml-raster) - Pure Standard ML 2D rasterizer: lines, rects, circles, triangles, polygons into RGBA8 images (MLton + Poly/ML).
- [sml-svg](https://github.com/sjqtentacles/sml-svg) - Pure Standard ML SVG document builder and pretty-printed serializer (MLton + Poly/ML).
- [sml-text-layout](https://github.com/sjqtentacles/sml-text-layout) - Pure-SML Unicode-aware text layout: greedy line breaking, word wrap, and grapheme-cluster measurement on bitmap fonts. Deterministic, byte-identical on MLton and Poly/ML.
- [sml-ui](https://github.com/sjqtentacles/sml-ui) - Pure, self-drawn immediate-mode GUI toolkit for Standard ML - deterministic, byte-identical rendering across MLton and Poly/ML, tested headlessly with golden images.

### Audio & music

Synthesis, MIDI, music theory and audio file formats. 5 libraries.

- [sml-midi](https://github.com/sjqtentacles/sml-midi) - Pure Standard ML Standard MIDI File (SMF) reader/writer: format 0 and 1, full event model, VLQ codec (MLton + Poly/ML).
- [sml-music](https://github.com/sjqtentacles/sml-music) - Pure Standard ML music theory: pitches, MIDI, frequencies, scales, chords, and key signatures (MLton + Poly/ML).
- [sml-score](https://github.com/sjqtentacles/sml-score) - Musical score data model in pure Standard ML, built on sml-music and sml-midi: rational beat durations, chords/scales, transposition, and Standard MIDI File rendering (MLton + Poly/ML).
- [sml-sequencer](https://github.com/sjqtentacles/sml-sequencer) - Step/event sequencer and drum machine in pure Standard ML on sml-midi + sml-music: grid patterns, GM drums, Euclidean (Bjorklund) rhythms, and Standard MIDI File output (MLton + Poly/ML).
- [sml-synth](https://github.com/sjqtentacles/sml-synth) - Higher-level music synthesis in pure Standard ML: wavetable, additive & FM synthesis, voices/ADSR, polyphonic mixdown, WAV export (MLton + Poly/ML).

### Games & simulation

Game-dev building blocks: ECS, AI, procedural generation, collision and cellular automata. 17 libraries.

- [sml-automata](https://github.com/sjqtentacles/sml-automata) - Cellular automata in pure Standard ML: Wolfram elementary rules and Conway's Game of Life (MLton + Poly/ML).
- [sml-bsp](https://github.com/sjqtentacles/sml-bsp) - Binary Space Partitioning dungeon generator with rooms and corridors in pure Standard ML.
- [sml-checkers](https://github.com/sjqtentacles/sml-checkers) - English draughts (checkers) with mandatory captures and search in pure Standard ML.
- [sml-chess](https://github.com/sjqtentacles/sml-chess) - Pure Standard ML chess core: fully legal move generation, perft, FEN, UCI, and a negamax search (MLton + Poly/ML).
- [sml-connect4](https://github.com/sjqtentacles/sml-connect4) - Connect Four engine with alpha-beta search in pure Standard ML.
- [sml-dice](https://github.com/sjqtentacles/sml-dice) - RPG dice notation evaluator with exact distributions in pure Standard ML.
- [sml-ecs](https://github.com/sjqtentacles/sml-ecs) - Entity-Component-System (ECS) architecture with sparse component stores in pure Standard ML.
- [sml-fov](https://github.com/sjqtentacles/sml-fov) - Recursive shadowcasting field-of-view and Bresenham line-of-sight for tile games in pure Standard ML.
- [sml-fsm](https://github.com/sjqtentacles/sml-fsm) - Finite state machine and behavior tree for game AI in pure Standard ML.
- [sml-gametree](https://github.com/sjqtentacles/sml-gametree) - Generic adversarial game-tree search (negamax/alpha-beta/PVS/IDAB) in pure Standard ML.
- [sml-mancala](https://github.com/sjqtentacles/sml-mancala) - Kalah (Mancala) with sowing, captures, extra turns, and search in pure Standard ML.
- [sml-maze](https://github.com/sjqtentacles/sml-maze) - Seeded maze generation (DFS/Prim/Kruskal/Wilson) and solving in pure Standard ML.
- [sml-nim](https://github.com/sjqtentacles/sml-nim) - Nim and Sprague-Grundy combinatorial game theory in pure Standard ML.
- [sml-othello](https://github.com/sjqtentacles/sml-othello) - Reversi/Othello engine with disc flipping and alpha-beta search in pure Standard ML.
- [sml-roguelike](https://github.com/sjqtentacles/sml-roguelike) - Roguelike building blocks (Brogue-style flow maps, autotiling, deterministic seeded placement) on top of sml-astar, in pure Standard ML for MLton and Poly/ML.
- [sml-tictactoe](https://github.com/sjqtentacles/sml-tictactoe) - M,n,k-game (tic-tac-toe/gomoku) with perfect-play minimax search in pure Standard ML. MLton + Poly/ML.
- [sml-tween](https://github.com/sjqtentacles/sml-tween) - 30 easing functions and keyframe timeline tweening in pure Standard ML.

### Concurrency, effects & systems

Async runtimes, structured concurrency, effect handlers, FRP, resilience, observability and distributed-systems building blocks. 25 libraries.

- [sml-actor](https://github.com/sjqtentacles/sml-actor) - Cooperative actor mailboxes built on FIFO channels for Standard ML.
- [sml-async](https://github.com/sjqtentacles/sml-async) - A portable, deterministic async library for Standard ML (scheduler + futures + async monad), running identically on MLton and Poly/ML.
- [sml-chan](https://github.com/sjqtentacles/sml-chan) - Buffered FIFO channels and a sequential process runner for Standard ML.
- [sml-circuit](https://github.com/sjqtentacles/sml-circuit) - Resilience primitives in pure Standard ML: circuit breaker, retry with backoff + jitter, rate limiter, bulkhead (MLton + Poly/ML).
- [sml-consistenthash](https://github.com/sjqtentacles/sml-consistenthash) - Consistent hashing ring with virtual nodes in pure Standard ML (CRC32-based). Minimal remapping on membership change. MLton + Poly/ML.
- [sml-crdt](https://github.com/sjqtentacles/sml-crdt) - A Standard ML library of state-based CRDTs: G-Counter, PN-Counter, LWW-Register, and OR-Set.
- [sml-cron](https://github.com/sjqtentacles/sml-cron) - Cron expression parser & schedule calculator in pure Standard ML: next/prev firing times. Time is an input. MLton + Poly/ML.
- [sml-csp](https://github.com/sjqtentacles/sml-csp) - CSP channels and structured concurrency in pure Standard ML on a deterministic virtual-time scheduler.
- [sml-effects](https://github.com/sjqtentacles/sml-effects) - Algebraic effects and handlers (State/Reader/Writer/Exception/Nondet) via a free-monad tree in pure Standard ML.
- [sml-gossip](https://github.com/sjqtentacles/sml-gossip) - SWIM-style gossip membership & failure detection simulated as a pure deterministic state machine in Standard ML (seeded PRNG). MLton + Poly/ML.
- [sml-hlc](https://github.com/sjqtentacles/sml-hlc) - Hybrid logical clocks (HLC) in pure Standard ML: physical+logical timestamps with bounded drift. Physical time is an input. MLton + Poly/ML.
- [sml-lens](https://github.com/sjqtentacles/sml-lens) - Concrete getter/setter optics (lenses, prisms, traversals, isos) in pure Standard ML.
- [sml-log](https://github.com/sjqtentacles/sml-log) - Leveled structured logging for Standard ML with a pluggable sink (default deterministic string sink). Pure, dual-compiler (MLton + Poly/ML).
- [sml-metrics](https://github.com/sjqtentacles/sml-metrics) - Prometheus-style counters, gauges, histograms + text exposition in pure Standard ML (MLton + Poly/ML).
- [sml-otel](https://github.com/sjqtentacles/sml-otel) - An OpenTelemetry trace and span model with W3C traceparent context propagation for Standard ML.
- [sml-prom](https://github.com/sjqtentacles/sml-prom) - Prometheus text exposition format generation for Standard ML.
- [sml-raft](https://github.com/sjqtentacles/sml-raft) - Raft consensus as a pure deterministic state machine in Standard ML: leader election, log replication, commit quorum (MLton + Poly/ML).
- [sml-ratelimit](https://github.com/sjqtentacles/sml-ratelimit) - Rate limiters as pure values in Standard ML: token bucket, leaky bucket, sliding window. Time is an input. MLton + Poly/ML.
- [sml-recscheme](https://github.com/sjqtentacles/sml-recscheme) - Recursion schemes (cata/ana/para/hylo) over functor fixpoints in pure Standard ML.
- [sml-signal](https://github.com/sjqtentacles/sml-signal) - Pure-SML functional reactive programming: deterministic time-varying signals and event streams (map/combine/foldp), no clock or FFI, byte-identical on MLton and Poly/ML.
- [sml-stm](https://github.com/sjqtentacles/sml-stm) - A single-threaded software transactional memory API with all-or-nothing rollback for Standard ML.
- [sml-stream](https://github.com/sjqtentacles/sml-stream) - Pure Standard ML lazy, fairly-interleaving streams (MLton + Poly/ML).
- [sml-trace](https://github.com/sjqtentacles/sml-trace) - OpenTelemetry-aligned tracing in pure Standard ML: spans, W3C traceparent codec, OTLP/JSON export (MLton + Poly/ML).
- [sml-transducer](https://github.com/sjqtentacles/sml-transducer) - Composable, fused transducers (map/filter/take/mapcat/dedupe) in pure Standard ML.
- [sml-vectorclock](https://github.com/sjqtentacles/sml-vectorclock) - Vector clocks for causal ordering in distributed systems, pure Standard ML: tick, merge (LUB), and happens-before comparison. Deterministic, MLton + Poly/ML.

### Databases & storage

Key-value stores, embedded databases and query engines. 7 libraries.

- [sml-kv](https://github.com/sjqtentacles/sml-kv) - A pure Standard ML log-structured key/value store model: append-only log, replay, compaction, length-prefixed serialization, and an SSTable binary-search block (MLton + Poly/ML).
- [sml-mvcc](https://github.com/sjqtentacles/sml-mvcc) - Multi-version concurrency control store as a pure value in Standard ML: snapshot isolation, first-committer-wins, GC. MLton + Poly/ML.
- [sml-pager](https://github.com/sjqtentacles/sml-pager) - Database buffer pool / page cache in pure Standard ML built on an LRU policy: dirty tracking, flush, eviction stats. MLton + Poly/ML.
- [sml-sheet](https://github.com/sjqtentacles/sml-sheet) - A pure Standard ML spreadsheet engine: A1 addressing, recursive-descent formula parser, and dependency-ordered recalc with cycle detection (MLton + Poly/ML).
- [sml-sql](https://github.com/sjqtentacles/sml-sql) - Pure in-memory SQL query engine (tokenizer + recursive-descent parser + evaluator) in Standard ML, no dependencies.
- [sml-wal](https://github.com/sjqtentacles/sml-wal) - Write-ahead log as a pure value in Standard ML: CRC32-framed records, checkpointing, and crash-safe replay. Byte-identical on MLton + Poly/ML.
- [sml-xlsx](https://github.com/sjqtentacles/sml-xlsx) - Pure Standard ML .xlsx (Office Open XML) reader/writer: sheets, shared strings, formulas.

### GUI, terminal & application UI

Windowing, immediate-mode GUIs, TUIs and UI architectures. 5 libraries.

- [sml-ansi](https://github.com/sjqtentacles/sml-ansi) - An ANSI/VT escape-sequence parser that turns terminal output into structured fragments for Standard ML.
- [sml-tea](https://github.com/sjqtentacles/sml-tea) - The Elm Architecture in pure Standard ML: Model-View-Update with zero-FFI server-side rendering, sml-vdom patches, sml-css styling, and sml-signal subscriptions. Dual-compiler (MLton + Poly/ML), byte-identical, deterministic.
- [sml-tui](https://github.com/sjqtentacles/sml-tui) - Pure Elm-architecture terminal UI toolkit for Standard ML: declarative widgets, an immutable screen buffer, and ANSI rendering with zero FFI (MLton + Poly/ML).
- [sml-vt](https://github.com/sjqtentacles/sml-vt) - A minimal VT-style fixed-size terminal grid for Standard ML.
- [sml-window](https://github.com/sjqtentacles/sml-window) - Impure minifb desktop-window backend for the pure sml-ui toolkit: opens a real OS window and runs the live interactive widget demo (MLton FFI, macOS). Quarantined impure tool.

### Text, Unicode & utilities

Unicode handling, date/time, configuration, randomness and IDs. 12 libraries.

- [sml-cli](https://github.com/sjqtentacles/sml-cli) - A Standard ML declarative command-line argument parser with subcommands and auto-generated help.
- [sml-collate](https://github.com/sjqtentacles/sml-collate) - Unicode-aware string collation producing linguistic sort keys for Standard ML.
- [sml-config](https://github.com/sjqtentacles/sml-config) - Typed config for Standard ML from a pure key/value source (env map / dotenv): required/optional/defaults with typed coercion. Pure, dual-compiler.
- [sml-datetime](https://github.com/sjqtentacles/sml-datetime) - Civil date arithmetic for Standard ML (MLton + Poly/ML): leap years, epoch days, addDays/diffDays, dayOfWeek, ISO-8601. Branch-free days-from-civil.
- [sml-ical](https://github.com/sjqtentacles/sml-ical) - iCalendar (RFC 5545) VEVENT parsing and RRULE recurrence expansion for Standard ML.
- [sml-ini](https://github.com/sjqtentacles/sml-ini) - INI configuration parser and serializer in pure Standard ML: sections, comments, quoted values, idempotent round-trip. MLton + Poly/ML.
- [sml-msgfmt](https://github.com/sjqtentacles/sml-msgfmt) - A tiny message plural-form selector (one/few/other) for Standard ML.
- [sml-prng](https://github.com/sjqtentacles/sml-prng) - Deterministic pseudo-random number generators for Standard ML (MLton + Poly/ML): SplitMix64, xoshiro256, PCG, uniform reals/ranges. Golden-vector tested, FFI-free.
- [sml-random](https://github.com/sjqtentacles/sml-random) - Splittable deterministic PRNG (SplitMix64) for Standard ML: tokens, nonces, session IDs. Reproducible seeded streams. Pure, dual-compiler.
- [sml-tzdb](https://github.com/sjqtentacles/sml-tzdb) - UTC-offset lookup for a small hand-coded set of timezones with simple DST rules for Standard ML.
- [sml-unicode](https://github.com/sjqtentacles/sml-unicode) - Unicode utilities for Standard ML: UTF-8/UTF-16 codecs, NFC/NFD normalization, case folding, grapheme segmentation, and display width. Pure, dual-compiler.
- [sml-uuid](https://github.com/sjqtentacles/sml-uuid) - RFC 4122/9562 UUID parse, format, and generate for Standard ML (MLton + Poly/ML): v4 + v7, deterministic (caller-supplied randomness), I/O-free.

### Misc

Libraries that do not yet fit a category above. 4 libraries.

- [awesome-standard-ml](https://github.com/sjqtentacles/awesome-standard-ml) - A curated list of Standard ML resources + an auto-generated index of the 240+ sjqtentacles sml-* ecosystem.
- [sml-fol](https://github.com/sjqtentacles/sml-fol) - First-order logic: parser, Skolemization, tableaux and resolution provers in pure SML.
- [sml-modal](https://github.com/sjqtentacles/sml-modal) - Propositional modal logic (K/T/S4/S5): tableau and Kripke model engines in pure SML.
- [sml-sequent](https://github.com/sjqtentacles/sml-sequent) - Gentzen LK/LJ sequent calculi for propositional logic in pure Standard ML: proof search, derivation checker, cut elimination (MLton + Poly/ML).
<!-- END GENERATED -->

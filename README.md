# Print Pretty Tree

`print_pretty_tree` is a simple Python script that displays the directory tree of the current working directory with color-coded output for easy file identification.

<p align="center">
  <img width="460"  src="https://i.imgur.com/GSO6vmJ.jpg">
</p>

<div align="center">

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/itsbrex/print-pretty-tree/CI?color=5ccfd6&style=flat-square)](https://github.com/itsbrex/print_pretty_tree/ac-io-s/workflows/release_to_pypi.yml) 

[![npm](https://img.shields.io/npm/v/print_pretty_tree?color-5-cfd6&style=flat-square)](https://www.npmjs.com/package/print-pretty-tree) [![npm](https://img.shields.io/npm/dt/print_pretty_tree?color-5-cfd6&style=flat-square)](https://www.npmjs.com/package/print-pretty-tree) [![GitHub](https://img.shields.io/github/license/itsbrex/print_pretty_tree?color-5-cfd6&style=flat-square)](https://github.com/itsbrex/print_pretty_tree/blob--ain/LICENSE)

</div>

## Installation  
To install `print_pretty_tree` globally, use your preferred package manager like `pnpm`, `yarn`, `npm`, or `bun`.
```bash
pnpm i -g print_pretty_tree
```
## Usage  
Navigate to any folder and run `print_pretty_tree`. The script will recursively pretty print the directory structure.
>By default, `print_pretty_tree` excludes certain folders and file patterns like `node_modules` and `.git` to make the output more manageable.  

If installed globally, you can just run `print_pretty_tree` in any directory:
```bash
print_pretty_tree
```

Or via `npx`:
```bash
npx print_pretty_tree
```


## Customization
- To add more file types and colors to the output, you can modify the `FILE_TYPE_COLORS` dictionary in the script.
- You can also customize the excluded file patterns by modifying the `EXCLUDED_PATTERNS` list in the script.

## Contributing 

If you find any bugs or want to suggest new features for `print_pretty_tree`, please feel free to contribute by submitting an issue or pull request.

Contributions are welcomed! This project follows the all-contributors spec. ([emoji key](https://github.com/all-contributors/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/github/all-contributors/itsbrex/print_pretty_tree?color=ee8449&style=flat-square)](#Contributing)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->


## License

Licensed under the MIT license. See the [LICENSE](./LICENSE) file for more information.

If you found this project interesting, please consider [sponsoring me](https://github.com/sponsors/itsbrex) or <a href="https://twitter.com/itsbrex">following me on twitter <img src="https://storage.googleapis.com/saasify-assets/twitter-logo.svg" alt="twitter" height="24px" align="center"></a>

# Print Pretty Tree

`print_pretty_tree` is a simple Python script that displays the directory tree of the current working directory with color-coded output for easy file identification.

<p align="center">
  <img width="460"  src="https://i.imgur.com/GSO6vmJ.jpg">
</p>

<div align="center">

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/itsbrex/print-pretty-tree/CI?color=5ccfd6&style=flat-square)](https://github.com/itsbrex/print-pretty-tree/actions/workflows/release_to_pypi.yml) 

[![npm](https://img.shields.io/npm/v/print-pretty-tree?color=5ccfd6&style=flat-square)](https://www.npmjs.com/package/print-pretty-tree) [![npm](https://img.shields.io/npm/dt/print-pretty-tree?color=5ccfd6&style=flat-square)](https://www.npmjs.com/package/print-pretty-tree) [![GitHub](https://img.shields.io/github/license/itsbrex/print-pretty-tree?color=5ccfd6&style=flat-square)](https://github.com/itsbrex/print-pretty-tree/blob/main/LICENSE)

</div>

## Installation

To install `print_pretty_tree`, you can use either `pip` or other package managers like `npm`, `pnpm`, or `yarn`.

### Install using pip

If you have Python and `pip` installed, you can run the following command:

```bash
pip install print_pretty_tree
```

### Install using other package managers

```bash
# Using npm
npm i -g print-pretty-tree

# Using pnpm
pnpm i -g print_pretty_tree

# Using yarn
yarn global add print-pretty-tree
```

## Usage

Once you have installed `print_pretty_tree`, you can run the script in any directory.

### Using pip installation

If you have installed `print_pretty_tree` using `pip`, you can run the following command in any directory:

```bash
print_pretty_tree
```

### Using other package managers

If you have installed the JavaScript version of `print_pretty_tree` using `npm`, `pnpm`, or `yarn`, you can run the following commands in any directory:

```bash
# Using npm, pnpm, or yarn
print-pretty-tree
```

By default, the script excludes certain folders and file patterns like `node_modules` and `.git` to make the output more manageable. The script will recursively pretty print the directory structure.


## Customization
- To add more file types and colors to the output, you can modify the `FILE_TYPE_COLORS` dictionary in the script.
- You can also customize the excluded file patterns by modifying the `EXCLUDED_PATTERNS` list in the script.

## Contributing 

If you find any bugs or want to suggest new features for `print_pretty_tree`, please feel free to contribute by submitting an [issue](https://github.com/itsbrex/print-pretty-tree/issues) or a [pull request](https://github.com/itsbrex/print-pretty-tree/pulls).

## Contributors ✨
Thanks goes to these wonderful people ([emoji key](https://github.com/all-contributors/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/github/all-contributors/itsbrex/print_pretty_tree?color=ee8449&style=flat-square)](#Contributing)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
This project follows the [all-contributors](https://allcontributors.org/) specification. Contributions of any kind welcome!

## License

Licensed under the MIT license. See the [LICENSE](./LICENSE) file for more information.

If you found this project interesting, please consider [sponsoring me](https://github.com/sponsors/itsbrex) or <a href="https://twitter.com/itsbrex">following me on twitter <img src="https://storage.googleapis.com/saasify-assets/twitter-logo.svg" alt="twitter" height="24px" align="center"></a>

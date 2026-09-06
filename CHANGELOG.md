# Changelog

## [Unreleased]

## [1.0.0] - 2026-09-06

### Breaking Changes
- Changed the translation API to require an explicit source language.
- Existing callers using the previous two-argument interface must be updated.

### Changed
- Translation output now includes source and target languages.

## [0.3.0] - 2026-09-06

### Added
- Improved system prompt for more focused and natural responses.
- Added instruction to avoid unnecessary explanations.
- Added instruction to preserve speaker tone and intent.

## [0.2.1] - 2026-09-06

### Fixed
- Fixed case-insensitive language selection.
- Normalized language input before translation.

## [0.2.0] - 2026-09-06

### Added
- Language selection for the Mini Interpreter.
- Support for Spanish, French, and German.
- Validation for unsupported languages.

## [0.1.0] - 2026-09-04

### Added
- Initial Mini Interpreter service.
- Basic translation interface.
- Initial system prompt.
- Initial product FAQ knowledge base.
- Basic test coverage.
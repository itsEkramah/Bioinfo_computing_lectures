"""
re — Regular expression notes for Python
Overview
--------
The 're' module provides regular expression (regex) support for searching, matching,
splitting and replacing strings using pattern descriptions. Regexes are powerful for
text processing, validation, parsing and pattern discovery (widely used in bioinformatics
for motif searches, sequence validation, parsing FASTA headers, etc.).
Basic usage patterns
--------------------
- import re
- re.search(pattern, string): return a Match object for the first location where
    the pattern matches, or None.
- re.match(pattern, string): check for a match only at the beginning of the string.
- re.fullmatch(pattern, string): match the whole string.
- re.findall(pattern, string): return a list of all non-overlapping matches as strings.
- re.finditer(pattern, string): return an iterator over Match objects.
- re.split(pattern, string, maxsplit=0): split string by occurrences of the pattern.
- re.sub(pattern, repl, string, count=0): replace matches with repl (string or callable).
- re.subn(...): like sub but also returns the number of substitutions.
- re.compile(pattern, flags=0): compile a pattern into a RegexObject for reuse (faster
    if used repeatedly).
Pattern syntax — important metacharacters
----------------------------------------
.       : matches any character except newline (unless DOTALL)
^       : match start of string (or start of line with MULTILINE)
$       : match end of string (or end of line with MULTILINE)
[]      : character class, e.g. [AGCT], [a-z0-9]
[^...]  : negated class, e.g. [^0-9]
|       : alternation (OR), e.g. cat|dog
()      : grouping and capturing
(?:...) : non-capturing group
\       : escape special characters; introduces escapes like \d, \w, \s
Common escape sequences
-----------------------
\d  : digit [0-9]
\D  : non-digit
\w  : word character [A-Za-z0-9_]
\W  : non-word
\s  : whitespace (space, tab, newline)
\S  : non-whitespace
\b  : word boundary
\B  : non-word-boundary
Use raw Python strings (r"...") to avoid Python-level backslash processing.
Quantifiers
-----------
*   : 0 or more (greedy)
+   : 1 or more (greedy)
?   : 0 or 1 (greedy)
{m,n} : between m and n repetitions
Greedy vs lazy: append ? to make quantifiers lazy (non-greedy), e.g. .*? or +?.
Groups and capturing
--------------------
- Parentheses capture substrings. Use match.group(n) or match.groups().
- Named groups: (?P<name>pattern) and access via match.group('name').
- Non-capturing groups: (?:pattern) when grouping without capturing.
- Backreferences in pattern: \1, \2 refer to capture groups.
Lookaround assertions (zero-width)
----------------------------------
- Positive lookahead: (?=...)
- Negative lookahead: (?!...)
- Positive lookbehind: (?<=...)
- Negative lookbehind: (?<!...)
Use lookarounds to assert context without consuming characters. Note: Python requires fixed-width lookbehind.
Flags (bitwise OR with patterns or compile)
-------------------------------------------
re.IGNORECASE (re.I)   : case-insensitive matching
re.MULTILINE (re.M)    : ^ and $ match at line boundaries
re.DOTALL (re.S)       : . matches newline too
re.VERBOSE (re.X)      : ignore whitespace and allow comments in pattern
re.ASCII (re.A)        : make \w, \b, \s, \d match only ASCII characters
Compilation and performance
---------------------------
- re.compile(pattern, flags) returns a pattern object. Reuse compiled patterns for
    repeated matches to improve performance.
- For large inputs or complex patterns, prefer finditer() over findall() when you need
    match objects (to avoid building large lists).
- Avoid catastrophic backtracking: nested quantifiers with ambiguous structure can be
    very slow on certain inputs. Use atomic grouping, more specific patterns, or possessive-
    style approaches (not directly supported in Python) to mitigate.
Common pitfalls and tips
------------------------
- Always use raw strings for patterns: r"\n" vs "\\n".
- Escape user-supplied strings with re.escape() before embedding them in regexes.
- Greedy quantifiers can overmatch; make them lazy (.*?).
- ^ and $ behavior changes with MULTILINE; use \A and \Z for absolute start/end.
- Use verbose mode (re.X) for complex patterns with comments and spacing.
- When matching Unicode text, be mindful of re.ASCII vs default Unicode behavior.
Examples
--------
- Find all 3-letter DNA codons: re.findall(r"[ACGT]{3}", sequence)
- Match FASTA header start: re.match(r"^>(\S+)", line)
- Replace runs of whitespace with a single space: re.sub(r"\s+", " ", text)
- Extract named group: m = re.search(r"(?P<id>gene\d+):(\d+)-(\d+)", s); m.group("id")
Bioinformatics notes
--------------------
- Use character classes for ambiguity codes (IUPAC). Example: R = [AG], Y = [CT], N = [ACGT].
- For motif searching with degeneracy, build character classes from IUPAC codes.
- Beware of overuse of '.' when working with sequence data; prefer explicit classes.
- For very large genomes or many queries, consider specialized libraries (e.g., regex
    module for advanced features, or sequence-specific tools) or algorithms (Aho–Corasick,
    suffix arrays) for speed.
Further reading
---------------
- Official Python docs: the re module reference (patterns, flags, examples)
- Practice with small patterns and progressively increase complexity; test with
    re.DEBUG or verbose mode when debugging tricky patterns.
"""

# Reference Edit bug fixes published — 14 October 2026

User authorized step 3: review/merge PR #2 and deploy through Sites. PR https://github.com/ivan-esteban23/the-reference-edit/pull/2 merged with an ordinary merge commit, `58ecf6fcac1c973902e7704758e32bf0df40ddbb`, preserving tested commit `b6660d750d5c710254846a5df3aaba07baec0cc0` in history. Exact reviewed head matched at merge; GitHub reported CLEAN/MERGEABLE with no checks configured. No admin override or force push. The feature branch is retained.

Local main was fast-forwarded to the merge commit. Complete tree comparison against the tested head passed; no source changes or redundant regression reruns were needed. Original regression evidence is copied into qa/: 96 layout cases, interaction/keyboard/accessibility-name/print checks, and actual offline migrations from both v42 and v43. See website tests/README.md and tests/RESULTS.md for reproducible commands and limits.

Native Sites source opened at v43 in the isolated site-source/ checkout, then fast-forwarded to the merged commit. Source helper verified the pushed source and packaged the unchanged static manifest/dist tree. Native save created version 44; native deployment succeeded at https://visual-edit-ivan.greymelon66.chatgpt.site. Public audience preserved. See deployment.json for opaque saved-version/deployment IDs and archive hash. Credential stayed in session memory and hidden helper stdin.

Production includes the full-body navigation deadline, shell v3 and translated-search recomputation; all 58 source records remain preserved. This task did not perform a production-origin browser migration or a physical-device installation test. Those are the next verification step. Obsidian publication notes and the vault HTML snapshot were not edited in this deployment task and still reflect their earlier snapshot date/version.

Standing end-of-task GitHub sync covers the seven merged website files, this recap, deployment receipt and saved QA evidence. Native source checkout and deployment tar remain local helper artifacts. No new website source commit was created after deployment.

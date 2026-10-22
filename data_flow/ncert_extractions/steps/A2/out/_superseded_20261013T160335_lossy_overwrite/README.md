# Superseded A2 output — the LOSSY side of a double-assignment race

Two agents were handed BIO11O-ch14-p009 at once (my error: I re-dispatched "stranded" pages while
the earlier wave was still running, so its in-flight items looked unassigned). Last-writer-wins
kept the weaker version, and the agent that lost said so explicitly:

  "BIO11O-ch14-p009.runA.json was rewritten on disk by another writer after I wrote it -- the
   replacement is substantively equivalent but drops `continues_from_previous` from several
   paragraph blocks and its note claims page 8 was unavailable; I left it in place rather than
   reverting."

This corrects something I wrote earlier today. I twice described these races as harmless because
"two agents reading the same page produce the same blocks, so the loser's output is equivalent".
That held for the three earlier collisions, where the difference was a 6px bbox or label joining.
It does NOT hold in general, and here it did not: continuation flags were lost and the surviving
note asserts something false about page 8. A race whose outcome is decided by write order can
preserve the worse answer, and "equivalent in the cases I checked" was not a safe generalisation.

Re-queued so one agent produces it cleanly with no competitor.

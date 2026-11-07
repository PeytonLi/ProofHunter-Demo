# ProofHunter checkout demo

Public, first-party examples for [ProofHunter](https://github.com/PeytonLi/ProofHunter).
Only `checkout.py` is enrolled for execution; this repository is not an arbitrary-code target.

## Reviewed contract

`checkout.total_cents(prices_cents: list[int], discount_percent: int) -> int`
implements `checkout-rounding@1`: sum integer cent prices, apply the integer discount,
then round the final total half up once.

```python
expected = (sum(prices_cents) * (100 - discount_percent) + 50) // 100
```

Inputs are bounded by the enrolled ProofHunter contract. The trusted oracle and
execution harness live in ProofHunter, not in this repository.

## Frozen demo branches

- `demo-base`: reviewed correct baseline. Keep this branch stable for pinned comparisons.
- `demo-buggy`: deliberately rounds discounted line items separately. For `[15, 15, 15]`
  at 10%, the baseline/oracle return 41 and this revision returns 42.
- `demo-fixed`: an equivalent correct refactor. The same example returns 41.

The two demonstration PRs target `demo-base` and are intentionally left open.
Do not merge the deliberately buggy PR. These branches copy the reviewed source
snapshots from ProofHunter's frozen fixtures; GitHub commit IDs are real, not fixture IDs.

## Local contract checks

For these reviewed examples only, use Python 3.12:

```bash
python -m unittest -v
```

The baseline and fixed branches pass. The buggy branch deliberately fails the
round-once examples. This small contract check is not an independent benchmark.

## Security and evidence

The dedicated GitHub App needs only Contents read, Pull requests read, and Metadata
read on this repository. Checks and webhooks remain disabled.

Publishing these examples does not establish a live ProofHunter pass. Live results
require exact source pinning, account/provider checks, an attested isolated Daytona
runner, receipt replay, and the independent release gates in the ProofHunter PRD.

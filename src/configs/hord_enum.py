from enum import Enum

class HordEnum(Enum):
    QUESTIONS_VALUES = [{"title": "What is ETH staking?", "value": "ETH staking is a process in which ETH holders can use their ETH to power the Ethereum blockchain"
                                                              " and earn rewards in the process."},
                        {"title": "What tokens can be staked?", "value":"Boosted APR in form of unlocked $HORD is given to stakers on Hord, "
                                                                    "with extra allocation for stETH and wstETH stakers."},
                        {"title": "What is hETH?", "value": "hETH is a token that represents the entire holdings in Hord’s ETH Staking pool. As validator rewards are added to"
                                                        " the pool, the price of hETH is expected to increase in relation to ETH."},
                        {"title": "Why is hETH price higher than Lido?", "value": "hETH's launch price was 2.53 ETH. This was due to the early accumulation of"
                                                                              " validator rewards before the pool was open to the public. While the price of hETH will continue"
                                                                              " to be higher than the price of ETH, this also means its value is higher, as the withdrawal power "
                                                                              "of 1 hETH is expected to grow over time as more rewards are earned by our validators." },
                        {"title": "What are HORD rewards?", "value": "Extra rewards are given to early adaptors in the form of tradable, unlocked HORD tokens. HORD will be used"
                                                                 " as Hord’s protocol token with in-app utility in the upcoming months. Details to be announced."},
                        {"title": "How can hETH be redeemed for ETH?", "value": "There are 2 options to get ETH back. Users can directly withdraw from the app by"
                                                                            " requesting a withdrawal, and then claiming their ETH. This can take up to 4 days depending"
                                                                            " on the withdrawal queue but is usually quicker. Alternatively, users can directly swap "
                                                                            "their hETH for ETH on Uniswap at any time."},
                        {"title": "What is the reward fee?", "value": "As a protocol, Hord takes a 10% fee of accumulated rewards, which goes towards operating the validators"
                                                                  " needed to stake ETH. To collect fees, Hord periodically mints proportional hETH representing its share."},
                        {"title": "What is Hord?", "value": "Hord is a Liquid ETH Staking protocol that maximizes staking rewards through auto-compounding, MEV boost and extra HORD"
                                                        " rewards. Hord is built by DcentraLab, an experienced web3 company with over $500M TVL"}
                        ]
from urllib.request import urlopen
from functools import reduce
import os


def fetchcoinMarketCaps(coinName):
	html = str(urlopen("https://coinmarketcap.com/currencies/" + coinName + "/historical-data/?start=20100101&end=20300101").read()) 

	indexStart = html.find("<td class=\"text-left\">",0, len(html))+22
	indexEnd = html.find("</td>\\n                        </tr>", indexStart, len(html))

	with open(os.getcwd()+"/data/"+coinName+".txt",'a') as coinFile:

		while indexStart != -1 and indexEnd-indexStart<1000:
			line = html[indexStart:indexEnd].replace("</td>\\n                        <td>", ";").replace(",", "")
			coinFile.write(line+'\n')
			indexStart = html.find("<td class=\"text-left\">",indexStart, len(html))+22
			indexEnd = html.find("</td>\\n                        </tr>", indexStart)

	coinFile.close()

listCoinNames = ['bitcoin', 'ethereum', 'ripple', 'bitcoin-cash', 'cardano', 'litecoin', 'nem', 'stellar', 'iota', 'dash', 'tron', 'neo', 'eos', 'monero', 'icon', 'bitcoin-gold', 'qtum', 'ethereum-classic', 'raiblocks', 'lisk', 'omisego', 'verge', 'siacoin', 'zcash', 'binance-coin', 'bitconnect', 'vechain', 'populous', 'bytecoin-bcn', 'kucoin-shares', 'stratis', 'bitshares', 'tether', 'status', 'ardor', 'dogecoin', 'augur', 'steem', 'waves', 'dragonchain', 'dentacoin', 'wax', 'digibyte', '0x', 'ark', 'veritaseum', 'komodo', 'hshare', 'dent', 'electroneum', 'golem-network-tokens', 'decred', 'basic-attention-token', 'pivx', 'qash', 'salt', 'gxshares', 'ethos', 'kyber-network', 'funfair', 'medibloc', 'kin', 'experience-points', 'bytom', 'reddcoin', 'factom', 'enigma-project', 'request-network', 'aion', 'aelf', 'aeternity', 'power-ledger', 'zclassic', 'substratum', 'nexus', 'byteball', 'digitalnote', 'rchain', 'monacoin', 'gas', 'maidsafecoin', 'nxt', 'neblio', 'walton', 'syscoin', 'zcoin', 'santiment', 'smartcash', 'gamecredits', 'iconomi', 'bitcoindark', 'digixdao', 'chainlink', 'gnosis-gno', 'cobinhood', 'achain', 'bancor', 'quantstamp', 'poet', 'tenx', 'blockv', 'raiden-network-token', 'civic', 'deepbrain-chain', 'storm', 'utrust', 'paccoin', 'skycoin', 'xplay', 'time-new-bank', 'vibe', 'ethlend', 'storj', 'red-pulse', 'airswap', 'emercoin', 'enjin-coin', 'pillar', 'vertcoin', 'paypie', 'counterparty', 'xtrabytes', 'blocknet', 'nav-coin', 'etherparty', 'cryptonex', 'aragon', 'centra', 'revain', 'sirin-labs-token', 'bridgecoin', 'monaco', 'wabi', 'simple-token', 'particl', 'bitbay', 'ripio-credit-network', 'edgeless', 'ubiq', 'naga', 'cindicator', 'decentraland', 'cybermiles', 'iot-chain', 'singulardtv', 'dynamic-trading-rights', 'sonm', 'rlc', 'streamr-datacoin', 'adx-net']
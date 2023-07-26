class stop_words():
    def __init__(self) -> None:
        pass
    stop_words_EN = {"abst",'accordance','according','accordingly','act','actually','added','adj','affected','affecting','affects','afterwards','ah','alone','along',
                    'already','although','always','amongst','announce','another','anybody','anyhow','anymore','anyone','anything','anyway','anyways','anywhere','apparently',
                    'approximately','arent','arise','around','aside','ask','asking','auth','available','away','awfully','back','became','become','becomes','becoming',"beforehand",
                    'begin','beginning','beginnings','begins','behind','believe','beside','besides','beyond','biol','brief','briefly','came','cause','causes','certain','certainly',
                    'co','com','come','comes','contain','containing','contains','couldnt','date','different','done','downwards','due','ed','edu','effect','eg','elsewhere','end',
                    'ending','enough','especially','et',"et-al","etc","even","everybody","everyone","everything","everywhere","ex","except","far","ff","fifth","five","fix","followed",
                    "following","follows","former","formerly","forth","found","four","furthermore","gave","gets","getting","give","given","gives","giving","go","goes","gone","gotten",
                    "happens","hardly","hed","hence","hereafter","hereby","herein",'heres','hereupon','hes','hi','hid','hither','howbeit','however','hundred','id','ie','im','immediate',
                    'immediately','importance','important','inc','indeed','index','instead','invention','inward','itd',"it'll","keep","keeps","kept","know","known","knows","largely",
                    "last","lately","later","latter","latterly","less","lest","lets","liked","line","'ll","look","looking","looks","mainly","make","makes","many","maybe","mean","means",
                    "meantime","meanwhile","merely","million","miss","moreover","mostly","much","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs",
                    "never","nevertheless","new","next","nobody","non","none","nonetheless","noone","normally","nos","noted","nothing","nowhere","obtain","obtained","obviously","oh","ok",
                    "okay","old","omitted","one","ones","onto","ord","others","otherwise","outside","overall","owing","past","per","perhaps","placed","please","poorly","possible",
                    "possibly","predominantly","previously","primarily","probably","promptly","put","que","quite","readily","really","recent","recently","regarding","regardless","regards",
                    "related","relatively","respectively","resulted","resulting","results","right","run","saw","saying","sec","section","see","seeing","seem","seemed","seeming",
                    "seems","seen","self","selves","sent","several","shall","shed","shes","show","showed","shown","showns","shows","significant","significantly","slightly","somebody","somehow",
                    "someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly",
                    "sub","substantially","successfully","sufficiently","suggest","sup","sure","take","taken","taking","tell","tends","th","thank","thanks","thanx","thats","that've",
                    'thence','thereafter','thereby','thered','therefore','therein',"there'll","thereof","therere","theres","thereto","thereupon","there've",'theyd','theyre','think','thou',
                    'though','thoughh','thousand','throug','throughout','thru','thus','til','tip','together','took','toward','towards','tried','tries','truly','try','trying','un','unfortunately',
                    'unless','unlike','unlikely','unto','upon','used','useful','usefully','usefulness','usually','various','ve','via','viz','want','wasnt','wed','welcome','went','werent',
                    'whatever',"what'll","who'll",'whats','whence','whenever','whereafter','whereas','whereby','wherein','wheres','whereupon','wherever','whether','whim','whither','whod',
                    'whoever','whole','whomever','whos','whose','widely','willing','wish','within','without','wont','words','world','wouldnt','www','x','yes','youd','youre','z','zero',"can't",
                    "he'd","he'll","he's","here's","how's","i'd","i'll","i'm","i've","let's","she'd","she'll","that's","there's","they'd","they'll","they're","they've",
                    "we'd","we'll","we're","we've","what's","when's","where's","who's","why's","ought",'able','across','almost','also','among','cannot','could','dear',
                    'either','else','ever','every','get','got','however, i','least','let','like','likely',
                    'may','might','must','neither','often','rather','said','say','says','since','tis','twas','us','wants','would','yet','d', 'he', 'she', "doesn't", 'too', 
                    'do', 'out', 'as', 've', 'who', 'because', 'from', 'when', 'ourselves', 'most', 'they', 'with', 'through', 'doing','mustn', 'some', 'haven', 'into', 
                    'shouldn', 'until', 'both', 's', 'has', "couldn't", 'there', 'themselves', 'at', 'm', 'have', "you've", 'no', 'won',
                    'wouldn', "won't", 'few', 'where', 'needn', 'against', 'to', 'such', 'be', 'i', 'y', 'why', "weren't", 'your', 'on', "hasn't", "wouldn't", 'mightn', 
                    'so', 'yours', 'theirs', 'been', 'herself', 'before', 'hasn', 're', 'my', 'while', 'off', "mustn't", 'or', "didn't", 'its', "aren't", 'couldn', 'how', 
                    'about', 'were', 'for', "should've", 'a', 'can', 'just', 'itself', "haven't", 'further', 'don', 'above', 'down', 'shan', 'nor', 'll', "don't", 'him', 
                    'hadn', "isn't", 'this', "shouldn't", 'the', 'all', 'only', "hadn't", 'whom', 'of', 'o', 'then', 'aren', 'by', 'are', 'and', 'yourselves', "you'd", 
                    'our', 'having', 'did', 't', 'does', "that'll", 'doesn', 'which', 'that', 'should', 'you', 'during', 'if', 'an', 'what', 'didn', 'yourself', 'in', 
                    "mightn't", 'ours', 'is', "needn't", 'but', "you'll", 'here', 'each', "it's", 'ain', 'his', 'same', 'more', 'their', 'weren', 'we', 'under', 'myself', 
                    'will', 'now', 'her', 'hers', "wasn't", 'once', 'these', 'am', 'than', 'up', 'those', 'had', 'between', "she's", 'it', 'again', 'any', 'being', 'me', 
                    "shan't", 'over', 'own', 'wasn', 'himself', 'them', 'was', 'after', 'below', 'other', 'very', 'ma', 'not', 'isn', "you're"}

    stop_words_PT = {"acerca",'algmas','ali','ambos','apontar','aqui','atrás','bem','bom','caminho','cima','comprido','conhecido','corrente','debaixo','dentro','desde',
                    'desligado','direita','dizer','dois','então','estado','estará','fará','faz','fazia','fez','fim','horas','iniciar','inicio','ir','irá','ista','iste',
                    'ligado','maioria','maiorias','nome','novo','onde','parte','pegar','pessoas','poderá','povo','promeiro','quê','qualquer','quieto','saber','somente',
                    'tal','tempo','tentar','tentaram','tente','tentei','tipo','trabalhar','trabalho','usa','usar','valor','veja','verdade','VERDADEIRO',
                    'agora','ainda','alguém','algum','alguma','algumas','alguns','ampla','amplas','amplo','amplos','ante','antes','após','através','cada','coisa','coisas',
                    'contra','contudo','daquele','daqueles','dessa','dessas','desse','desses','desta','destas','deste','destes','deve','devem','devendo','dever','deverá','deverão',
                    'deveria','deveriam','devia','deviam','disse','disso','disto','dito','diz','dizem','enquanto','fazendo','fazer','feita','feitas','feito','feitos','grande',
                    'grandes','la','lá','lo','mesma','mesmas','mesmos','muita','muitas','muitos','nenhum','nessa','nessas','nesta','nestas','ninguém','nunca','outra','outras',
                    'outro','outros','pequena','pequenas','pequeno','pequenos','per','perante','pode','pude','podendo','poder','poderia','poderiam','podia','podiam','pois','porém',
                    'porque','posso','pouca','poucas','pouco','poucos','primeiro','primeiros','própria','próprias','próprio','próprios','quais','quanto','quantos','sempre','sendo','si',
                    'sido','sob','sobre','talvez','tampouco','tendo','ti','tido','toda','todas','todavia','todo','todos','tudo','última','últimas','último','últimos','umas','uns','vendo',
                    'ver','vez','vindo','vir','vós','teriam', 'ter', 'têm', 'havia', 'hajam', 'serei', 'tivessem', 'esse', 'estejam', 'fossem', 'houverão', 'estávamos', 'houveram', 'nossas', 
                    'do', 'seu', 'mas','as', 'terá','não', 'até', 'delas', 'ela', 'tem', 'tivemos', 'à', 'ele', 'tivéssemos', 'e', 'tinha', 'tém', 'fomos', 'na', 'fôssemos', 'será', 'num', 'houverem', 
                    'mais', 'estivéramos', 'estão', 'tenha', 'da', 'há', 'tuas', 'minhas', 'aquele', 'essas', 'entre', 'houveria', 'tenho', 'teus', 'no', 'às', 'estivéssemos', 
                    'sem', 'estavam', 'éramos', 'terão', 'está', 'também', 'só', 'aquilo', 'somos', 'suas', 'tu', 'dele', 'numa', 'vos', 'nosso', 'por', 'esteja', 'haver', 
                    'estivera', 'tua', 'estejamos', 'pelas', 'minha', 'estivemos', 'eu', 'qual', 'temos', 'tenham', 'tinham', 'sejam', 'estiver', 'teu', 'estou', 'dos', 'os', 
                    'este', 'teve', 'muito', 'se', 'dela', 'for', 'a', 'teria', 'tive', 'houveríamos', 'nas', 'estava', 'houvessem', 'sou', 'tínhamos', 'elas', 'meu', 'tivesse', 
                    'quando', 'nem', 'pela', 'estar', 'você', 'de', 'hajamos', 'pelos', 'aquela', 'esses', 'nossos', 'houvéramos', 'para', 'seríamos', 'nossa', 'meus', 'fora', 
                    'seria', 'te', 'seriam', 'o', 'estiveram', 'forem', 'houverei', 'ser', 'estivessem', 'houver', 'estiverem', 'formos', 'aquelas', 'fui', 'isto', 'estivesse', 'já', 
                    'seremos', 'aos', 'tiveram', 'houverá', 'fôramos', 'houvera', 'esta', 'haja', 'das', 'é', 'tiverem', 'depois', 'ao', 'isso', 'sua', 'tivéramos', 'vocês', 'com', 
                    'essa', 'sejamos', 'estamos', 'houvermos', 'tenhamos', 'terei', 'houvéssemos', 'uma', 'lhe', 'serão', 'havemos', 'houveremos', 'tivera', 'seus', 'houvemos', 'houvesse', 
                    'foi', 'houve', 'teremos', 'como', 'tivermos', 'estes', 'que', 'aqueles', 'hão', 'um', 'são', 'mesmo', 'tiver', 'nós', 'em', 'estive', 'ou', 'nos', 'esteve', 
                    'quem', 'seja', 'era', 'hei', 'pelo', 'teríamos', 'estivermos', 'me', 'fosse', 'houveriam', 'eles', 'eram', 'estas', 'foram', 'lhes', 'deles'}
    


import spacy
from gensim.parsing.preprocessing import STOPWORDS
import nltk
from tqdm import tqdm
from nltk.corpus import stopwords
nltk.download('stopwords')



class string_validate(stop_words):
    def __init__(self, df, name_column='Item Title', column_response='nome ajustado') -> None:
        # self.dic()
        self.df = df
        self.nlp = spacy.load('pt_core_news_lg')
        # self.stop_words = set(STOPWORDS).union(set(self.nlp.Defaults.stop_words))
        # self.stop_words_en = set(stopwords.words('english'))
        self.stop_words = self.stop_words_PT
        self.stop_words_en = self.stop_words_EN
        tqdm.pandas()
        self.df[column_response] = self.df[name_column].progress_apply(lambda x: self._name_redux(x))

    def _name_redux(self, name):
        doc = self.nlp(name)
        words = [token.lemma_ for token in doc if token.is_alpha and token.lemma_ not in self.stop_words and token.lemma_ not in self.stop_words_en]
        return " ".join(words)

    # função para retornar df
    def get_response(self):
        return self.df
    
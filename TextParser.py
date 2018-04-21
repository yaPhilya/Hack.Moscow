import pymorphy2
import json
import webcolors

class TextParser:

    def __init__(self, stored_names, stored_paths):
        self.morph = pymorphy2.MorphAnalyzer()
        self.stored_names = {
            'яблоко': 'apple',
            'кресло': 'armchair',
            'медведь': 'bear',
            'лодка': 'boat',
            'книжный шкаф': 'bookCase',
            'бутылка': 'bottle',
            'здание': 'building',
            'автобус': 'bus',
            'бабочка': 'butterfly',
            'костер': 'campfire',
            'кошка': 'cat',
            'шимпанзе': 'chimp',
            'клоун': 'clownFish',
            'контейнер': 'container',
            'рак': 'crab',
            'олень': 'deer',
            'собака': 'dog',
            'дракон': 'dragon',
            'рыба': 'fish',
            'вилка': 'fork',
            'беседка': 'gazebo',
            'жираф': 'giraffe',
            'дом': 'house',
            'кружка': 'mug',
            'оранжевый': 'orange',
            'свинья': 'pig',
            'подушка': 'pillow',
            'носорог': 'rhino',
            'пауки': 'spiders',
            'ложка': 'spoon',
            'звездолет': 'starDestroyer',
            'пар': 'streamLocomotive',
            'таблица': 'table',
            'бак': 'tank',
            'чушка': 'teeCup',
            'дерево': 'tree',
            'деревья': 'trees',
            'трицератопс': 'triceratops',
            'волк': 'wolf'
        }
        self.color_map = {
'абрикосовый' : '#FBCEB1',
'абрикосовый крайола' : '#FDD9B5',
'агатовый серый' : '#B5B8B1',
'аквамариновый' : '#7FFFD4',
'аквамариновый крайола' : '#78DBE2',
'ализариновый красный' : '#E32636',
'алый' : '#FF2400',
'амарантово-пурпурный' : '#AB274F',
'амарантово-розовый' : '#F19CBB',
'амарантовый' : '#E52B50',
'амарантовый глубоко-пурпурный' : '#9F2B68',
'амарантовый маджента' : '#ED3CCA',
'амарантовый светло-вишневый' : '#CD2682',
'американский розовый' : '#FF033E',
'аметистовый' : '#9966CC',
'античная латунь' : '#CD9575',
'антрацитово-серый' : '#293133',
'антрацитовый' : '#464451',
'арлекин' : '#44944A',
'аспидно-серый' : '#2F4F4F',
'аспидно-синий' : '#6A5ACD',
'бабушкины яблоки' : '#A8E4A0',
'базальтово-серый' : '#4E5754',
'баклажанный крайола' : '#614051',
'баклажановый' : '#990066',
'баклажановый крайола' : '#6E5160',
'бананомания' : '#FAE7B5',
'барвинок  перванш' : '#CCCCFF',
'барвинок крайола' : '#C5D0E6',
'бедра испуганной нимфы' : '#FAEEDD',
'бежево-коричневый' : '#79553D',
'бежево-красный' : '#C1876B',
'бежево-серый' : '#6D6552',
'бежевый' : '#F5F5DC',
'бело-алюминиевый' : '#A5A5A5',
'бело-зеленый' : '#BDECB6',
'белоснежный' : '#FFFAFA',
'белый' : '#FFFFFF',
'белый антик' : '#FAEBD7',
'белый навахо' : '#FFDEAD',
'берлинская лазурь' : '#003153',
'бирюзово-голубой крайола' : '#77DDE7',
'бирюзово-зеленый' : '#1E5945',
'бирюзово-синий' : '#3F888F',
'бирюзовый' : '#30D5C8',
'бисквитный' : '#FFE4C4',
'бисмарк-фуриозо' : '#A5260A',
'бистр' : '#3D2B1F',
'бледно-васильковый' : '#ABCDEF',
'бледно-желтый' : '#FFDB8B',
'бледно-зелено-серый' : '#8D917A',
'бледно-зеленый' : '#89AC76',
'бледно-золотистый' : '#EEE8AA',
'бледно-карминный' : '#B03F35',
'бледно-каштановый' : '#DDADAF',
'бледно-коричневый' : '#755C48',
'бледно-песочный' : '#DABDAB',
'бледно-пурпурный' : '#F984E5',
'бледно-розоватый' : '#FFCBDB',
'бледно-розовый' : '#FADADD',
'бледно-синий' : '#AFEEEE',
'бледно-фиолетовый' : '#957B8D',
'бледный весенний бутон' : '#ECEBBD',
'бледный желто-зеленый' : '#F0D698',
'бледный желто-розовый' : '#FFC8A8',
'бледный зеленовато-желтый' : '#FFDF84',
'бледный зеленый' : '#98FB98',
'бледный красно-пурпурный' : '#AC7580',
'бледный оранжево-желтый' : '#FFCA86',
'бледный пурпурно-розовый' : '#FDBDBA',
'бледный пурпурно-синий' : '#8A7F8E',
'бледный серо-коричневый' : '#BC987E',
'бледный синий' : '#919192',
'бледный фиолетово-красный' : '#D87093',
'блестящий желто-зеленый' : '#CED23A',
'блестящий желтовато-зеленый' : '#8CCB5E',
'блестящий желтый' : '#FFCF40',
'блестящий зеленовато-желтый' : '#FFDC33',
'блестящий зеленовато-синий' : '#2A8D9C',
'блестящий зеленый' : '#47A76A',
'блестящий оранжевый' : '#FFB841',
'блестящий пурпурно-розовый' : '#FF97BB',
'блестящий пурпурно-синий' : '#62639B',
'блестящий пурпурный' : '#DD80CC',
'блестящий синевато-зеленый' : '#009B76',
'блестящий синий' : '#4285B4',
'блестящий фиолетовый' : '#755D9A',
'блошиный (красновато-коричневый)' : '#755A57',
'бобровый' : '#9F8170',
'болгарский розовый' : '#480607',
'болотный' : '#ACB78E',
'бордо (красно-бордовый)' : '#B00000',
'бордово-фиолетовый' : '#641C34',
'бордовый' : '#9B2D30',
'бороды абдель-керима' : '#D5D5D5',
'брезентово-серый' : '#4C514A',
'бриллиантово-синий' : '#3E5F8A',
'бриллиантовый оранжево-желтый' : '#FFB02E',
'бронзовый' : '#CD7F32',
'бургундский' : '#900020',
'бурый' : '#45161C',
'бутылочно-зеленый' : '#343B29',
'ванильный' : '#D5713F',
'васильковый' : '#6495ED',
'васильковый крайола' : '#9ACEEB',
'вердепешевый' : '#DAD871',
'вердепомовый' : '#34C924',
'вересково-фиолетовый' : '#DE4C8A',
'весенне-зеленый (зеленая весна)' : '#00FF7F',
'весенне-зеленый крайола' : '#ECEABE',
'весенний бутон' : '#A7FC00',
'византийский' : '#BD33A4',
'византия' : '#702963',
'винно-красный' : '#5E2129',
'винтовочный зеленый' : '#414833',
'вишневый (вишня)' : '#911E42',
'в меру оливково-коричневый' : '#64400F',
'водная синь' : '#256D7B',
'воды пляжа бонди' : '#0095B6',
'восход солнца' : '#FFCF48',
'галечный серый' : '#B8B799',
'гейнсборо' : '#DCDCDC',
'гелиотроп (гелиотроповый)' : '#DF73FF',
'георгиново-желтый' : '#F3A505',
'глиняный коричневый' : '#734222',
'глициния (глициниевый)' : '#C9A0DC',
'глициния крайола' : '#CDA4DE',
'глубокая фуксия крайола' : '#C154C1',
'глубокий желто-коричневый' : '#593315',
'глубокий желто-розовый' : '#F64A46',
'глубокий желтовато-зеленый' : '#00541F',
'глубокий желтый' : '#B57900',
'глубокий желтый зеленый' : '#425E17',
'глубокий зеленовато-желтый' : '#9F8200',
'глубокий зеленый' : '#004524',
'глубокий карминно-розовый' : '#EF3038',
'глубокий карминный' : '#A9203E',
'глубокий коралловый' : '#FF4040',
'глубокий коричневый' : '#4D220E',
'глубокий красно-коричневый' : '#490005',
'глубокий красно-оранжевый' : '#A91D11',
'глубокий красно-пурпурный' : '#641349',
'глубокий красный' : '#7B001C',
'глубокий оливково-зеленый' : '#142300',
'глубокий оранжево-желтый' : '#D76E00',
'глубокий оранжевый' : '#C34D0A',
'глубокий пурпурно-красный' : '#6F0035',
'глубокий пурпурно-розовый' : '#EB5284',
'глубокий пурпурно-синий' : '#1A153F',
'глубокий пурпурный' : '#531A50',
'глубокий розовый' : '#FF1493',
'глубокий синевато-зеленый' : '#00382B',
'глубокий синий' : '#002F55',
'глубокий фиолетово-черный' : '#240935',
'глубокий фиолетовый' : '#423189',
'голубино-синий' : '#606E8C',
'голубой' : '#42AAFF',
'голубой (морозное небо)' : '#00BFFF',
'голубой колокольчик крайола' : '#A2A2D0',
'голубой крайола' : '#80DAEB',
'горечавково-синий' : '#0E294B',
'горный луг' : '#30BA8F',
'городское небо (пасмурно-небесный)' : '#87CEEB',
'горчичный' : '#FFDB58',
'горько-сладкий' : '#FD7C6E',
'гранатовый' : '#F34723',
'гранитовый серый (гранитный)' : '#2F353B',
'графитно-черный' : '#1C1C1C',
'графитовый серый' : '#474A51',
'гридеперлевый' : '#C7D0CC',
'грузинский розовый' : '#D71868',
'грушево-зеленый' : '#D1E231',
'грушевый' : '#EFD334',
'гуммигут' : '#E49B0F',
'гусеница' : '#B2EC5D',
'дартмутский зеленый' : '#00693E',
'джазовый джем' : '#CA3767',
'джинсовый синий' : '#1560BD',
'дикая клубника крайола' : '#FF43A4',
'дикий арбуз крайола' : '#FC6C85',
'дикий синий крайола' : '#A2ADD0',
'дымчато-белый' : '#F5F5F5',
'дынно-желтый' : '#F4A900',
'дыня крайола' : '#FDBCB4',
'железно-серый' : '#434B4D',
'желтая сера' : '#EDFF21',
'желтая слоновая кость' : '#E1CC4F',
'желто-зеленый' : '#9ACD32',
'желто-зеленый крайола' : '#C5E384',
'желто-золотой' : '#CDA434',
'желто-оливковый' : '#47402E',
'желто-оранжевый' : '#ED760E',
'желто-оранжевый крайола' : '#FFAE42',
'желто-персиковый' : '#FADFAD',
'желто-розовый' : '#FFE4B2',
'желто-серый' : '#8F8B66',
'желтовато-белый' : '#FFE2B7',
'желтовато-серый' : '#CAA885',
'желтый' : '#FFFF00',
'желтый карри' : '#9D9101',
'желтый крайола' : '#FCE883',
'желтый ракитник' : '#D6AE01',
'жемчужно-белый' : '#EAE6CA',
'жженый апельсин (выгоревший оранжевый)' : '#CC5500',
'жимолость' : '#CB6586',
'защитно-синий' : '#1E90FF',
'защитный хаки (камуфляжный)' : '#78866B',
'звезды в шоке' : '#FF47CA',
'зеленая лужайка' : '#7CFC00',
'зеленая сосна' : '#01796F',
'зеленая сосна крайола' : '#158078',
'зелено-бежевый' : '#BEBD7F',
'зелено-желтый' : '#ADFF2F',
'зелено-желтый крайола' : '#F0E891',
'зелено-коричневый' : '#826C34',
'зелено-лаймовый' : '#BFFF00',
'зелено-серый' : '#4D5645',
'зелено-синий' : '#1F3438',
'зелено-синий крайола' : '#1164B4',
'зеленовато-белый' : '#F5E6CB',
'зеленовато-серый' : '#7A7666',
'зеленовато-черный' : '#181513',
'зеленоватый мокрый асфальт' : '#4E5452',
'зеленое море' : '#2E8B57',
'зеленые джунгли крайола' : '#3BB08F',
'зеленые джунгли крайола 90-го года' : '#29AB87',
'зеленый' : '#008000',
'зеленый крайола' : '#1CAC78',
'зеленый лишайник  мох (цвет зеленого мха)' : '#ADDFAD',
'зеленый мичиганского университета' : '#006633',
'зеленый мох' : '#2F4538',
'зеленый орел' : '#004953',
'зеленый папоротник' : '#4F7942',
'зеленый трилистник' : '#009A63',
'зеленый чай' : '#D0F0C0',
'золотарник крайола' : '#FCD975',
'золотисто-березовый' : '#DAA520',
'золотисто-каштановый' : '#712F26',
'золотой (золотистый)' : '#FFD700',
'золотой крайола' : '#E7C697',
'ивово-коричневый' : '#321414',
'известковая глина' : '#79443B',
'изумруд' : '#009B77',
'изумрудно-зеленый' : '#287233',
'изумрудный' : '#50C878',
'индиго' : '#4B0082',
'индиго крайола' : '#5D76CB',
'индийский зеленый' : '#138808',
'индийский красный  каштановый' : '#CD5C5C',
'ирландский зеленый' : '#4CBB17',
'июньский бутон' : '#BDDA57',
'кадетский синий' : '#5F9EA0',
'кадетский синий крайола' : '#B0B7C6',
'камелопардовый' : '#A25F2A',
'каменно-серый' : '#8B8C7A',
'канареечный (ярко-желтый)' : '#FFFF99',
'капри синий' : '#1B5583',
'кардинал' : '#C41E3A',
'карибский зеленый' : '#1CD3A2',
'кармин' : '#960018',
'карминно-красный' : '#A2231D',
'карминно-розовый' : '#EB4C42',
'карминово-красный' : '#FF0033',
'каштаново-коричневый' : '#633A34',
'каштановый крайола' : '#BC5D58',
'кварцевый' : '#99958C',
'кварцевый серый' : '#6C6960',
'киноварь' : '#FF4D00',
'кирпично-красный' : '#CB4154',
'кирпичный' : '#884535',
'китайский красный (киноварь)' : '#E34234',
'кленовый зеленый' : '#507D2A',
'клубнично-красный' : '#D53032',
'кобальтово-синий' : '#1E213D',
'кобальт синий (кобальтовый)' : '#0047AB',
'кожа буйвола (палевый)' : '#F0DC82',
'кожура апельсина' : '#FFA000',
'кораллово-красный' : '#B32821',
'коралловый' : '#FF7F50',
'кордованский' : '#893F45',
'коричневато-оранжевый' : '#B15124',
'коричневато-розовый' : '#CD9A7B',
'коричневато-серый' : '#503D33',
'коричневато-черный' : '#140F0B',
'коричнево-бежевый' : '#8A6642',
'коричнево-бордовый' : '#A52A2A',
'коричнево-желтый цвета увядших листьев' : '#C19A6B',
'коричнево-зеленый' : '#39352A',
'коричнево-красный' : '#781F19',
'коричнево-малиновый' : '#800000',
'коричнево-малиновый крайола' : '#C8385A',
'коричнево-оливковый' : '#25221B',
'коричневый' : '#964B00',
'коричневый крайола' : '#B4674D',
'коричневый серый' : '#464531',
'коричневый цвета кожанного седла для лошади' : '#8B4513',
'коричный' : '#7B3F00',
'королевская фуксия' : '#CA2C92',
'королевский пурпурный крайола' : '#7851A9',
'королевский синий' : '#4169E1',
'космические сливки' : '#FFF8E7',
'космос' : '#414A4C',
'кофейный' : '#442D25',
'крайоловый абрикос' : '#FDD5B1',
'красно-буро-оранжевый' : '#CD5700',
'красно-желто-коричневый' : '#80461B',
'красно-коричневый' : '#592321',
'красно-оранжевый' : '#C93C20',
'красно-оранжевый крайола' : '#FF5349',
'красно-сиреневый' : '#6D3F5B',
'красно-фиолетовый' : '#922B3E',
'красно-фиолетовый крайола' : '#C0448F',
'красновато-серый' : '#8B6C62',
'красновато-черный' : '#1E1112',
'красное дерево' : '#C04000',
'красное дерево крайола' : '#CD4A4C',
'красный' : '#FF0000',
'красный крайола' : '#EE204D',
'красный песок' : '#F4A460',
'кремово-желтый' : '#FFFDD0',
'кремовый' : '#FDF4E3',
'кремовый хаки' : '#C3B091',
'кричащий зеленый' : '#76FF7A',
'крутой розовый крайола' : '#FB607F',
'кукурузно-желтый' : '#E4A010',
'кукурузный' : '#FBEC5D',
'лаванда (лавандовый)' : '#E6E6FA',
'лавандовый крайола' : '#FCB4D5',
'лавандовый розовый' : '#FBA0E3',
'лазерный лимон' : '#FEFE22',
'лазурно-серый (зеленовато-синий)' : '#007BA7',
'лазурно-синий' : '#025669',
'лазурный  азур' : '#007FFF',
'лазурный крайола' : '#1DACD6',
'лайм' : '#00FF00',
'лаймово-зеленый' : '#32CD32',
'ламантин' : '#979AAA',
'латунный' : '#B5A642',
'лесной волк' : '#DBD7D2',
'лесной зеленый' : '#228B22',
'ливерный' : '#534B4F',
'лиловый' : '#DB7093',
'лимонно-желтый' : '#C7B446',
'лимонно-желтый крайола' : '#FFF44F',
'лимонно-кремовый' : '#FFFACD',
'лимонный' : '#FDE910',
'лиственно-зеленый' : '#2D572C',
'лиственный зеленый крайола' : '#6DAE81',
'лососево-красный' : '#D95030',
'лососево-оранжевый' : '#E55137',
'лососевый' : '#FF8C69',
'лососевый крайола' : '#FF9BAA',
'льняной' : '#FAF0E6',
'люминесцентный красный' : '#F80000',
'люминесцентный ярко-оранжевый' : '#FFA420',
'лягушка в обмороке' : '#7B917B',
'магическая мята' : '#AAF0D1',
'магнолия' : '#F8F4FF',
'маджента  фуксия (пурпурный)' : '#FF00FF',
'маджента крайола' : '#F664AF',
'маисовый' : '#EDD19C',
'майский зеленый' : '#4C9141',
'макароны и сыр' : '#FFBD88',
'малахитовый' : '#0BDA51',
'малиново-красный' : '#C51D34',
'малиново-розовый' : '#B3446C',
'малиновый' : '#DC143C',
'мальва (розовато-лиловый)' : '#993366',
'манго-танго' : '#FF8243',
'мандариновое танго' : '#E1523D',
'мандариновый' : '#FF8800',
'маренго' : '#4C5866',
'марсала' : '#AD655F',
'махагон коричневый' : '#4C2F27',
'медно-коричневый' : '#8E402A',
'медно-розовый (бледный розовато-лиловый)' : '#996666',
'медный' : '#B87333',
'медный крайола' : '#DD9475',
'медовая роса' : '#F0FFF0',
'медово-желтый' : '#A98307',
'медовый' : '#FEE5AC',
'международный оранжевый (сигнальный)' : '#FF4F00',
'мертвенный индиго' : '#00416A',
'миндаль крайола' : '#EFDECD',
'миртовый' : '#21421E',
'мовеин (анилиновый пурпур)' : '#EF0097',
'модная фуксия' : '#F400A1',
'мокасиновый' : '#FFE4B5',
'мокрый тропический лес' : '#17806D',
'морковный' : '#F36223',
'морской зеленый' : '#54FF9F',
'морской зеленый крайола' : '#9FE2BF',
'мурена' : '#1C6B72',
'мусульманский зеленый' : '#009900',
'мышино-серый' : '#646B63',
'мята (цвет зеленой мяты)' : '#98FF98',
'мятно-бирюзовый' : '#497E76',
'мятно-зеленый' : '#20603D',
'мятно-кремовый' : '#F5FFFA',
'мятный' : '#3EB489',
'нарциссово-желтый' : '#DC9D00',
'насыщенный желто-зеленый' : '#7F8F18',
'насыщенный желто-коричневый' : '#95500C',
'насыщенный желто-розовый' : '#FF7A5C',
'насыщенный желтовато-зеленый' : '#478430',
'насыщенный желтый' : '#E59E1F',
'насыщенный зеленовато-желтый' : '#CCA817',
'насыщенный зеленовато-синий' : '#00677E',
'насыщенный зеленый' : '#006B3C',
'насыщенный коричневый' : '#753313',
'насыщенный красно-коричневый' : '#7F180D',
'насыщенный красно-оранжевый' : '#FFB961',
'насыщенный красно-пурпурный' : '#9A366B',
'насыщенный красный' : '#BF2233',
'насыщенный оливково-зеленый' : '#0A4500',
'насыщенный оранжево-желтый' : '#FF8E0D',
'насыщенный оранжевый' : '#EC7C26',
'насыщенный пурпурно-красный' : '#B32851',
'насыщенный пурпурно-розовый' : '#F6768E',
'насыщенный пурпурно-синий' : '#474389',
'насыщенный розовый' : '#FD7B7C',
'насыщенный синевато-зеленый' : '#006D5B',
'насыщенный синий' : '#00538A',
'насыщенный фиолетовый' : '#53377A',
'натуральная умбра' : '#734A12',
'небесная лазурь' : '#F0FFFF',
'небесно-синий' : '#2271B3',
'небесный' : '#7FC7FF',
'нежно-оливковый' : '#6B8E23',
'незрелый желтый' : '#FFFF66',
'неоново-морковный' : '#FFA343',
'нефритовый' : '#00A86B',
'ниагара' : '#9DB1CC',
'ночной синий' : '#252850',
'обычный весенний бутон' : '#C9DC87',
'огненная сиенна крайола' : '#EA7E5D',
'огненно-красный' : '#AF2B1E',
'огненный оранжевый' : '#FF7F49',
'одуванчиковый' : '#FDDB6D',
'океанская синь' : '#1D334A',
'оксид красный' : '#642424',
'олень коричневый' : '#59351F',
'оливково-желтый' : '#999950',
'оливково-зеленый' : '#424632',
'оливково-зеленый крайола' : '#BAB86C',
'оливково-коричневый' : '#6F4F28',
'оливково-черный' : '#121910',
'оливковый' : '#808000',
'оливковый серый' : '#4D4234',
'опаловый зеленый' : '#015D52',
'оперный розовато-лиловый' : '#B784A7',
'оранжевая заря' : '#FD5E53',
'оранжево-желтый крайола' : '#F8D568',
'оранжево-коричневый' : '#A65E2E',
'оранжево-красный крайола' : '#FF2B2B',
'оранжево-персиковый' : '#FFCC99',
'оранжево-розовый' : '#FF9966',
'оранжевый' : '#FFA500',
'оранжевый крайола' : '#FF7538',
'орехово-коричневый' : '#5B3A29',
'ориент красный' : '#B32428',
'орхидея' : '#DA70D6',
'орхидея крайола' : '#E6A8D7',
'отборный желтый' : '#FFBA00',
'отдаленно-синий' : '#49678D',
'охотничий зеленый' : '#355E3B',
'охра' : '#CC7722',
'охра желтая' : '#AEA04B',
'охра коричневая' : '#955F20',
'очень бледно-пурпурный' : '#E6BBC1',
'очень бледный зеленый' : '#D8DEBA',
'очень бледный пурпурно-синий' : '#CBBAC5',
'очень бледный синий' : '#C1CACA',
'очень бледный фиолетовый' : '#D8B1BF',
'очень глубокий желто-зеленый' : '#002800',
'очень глубокий красно-пурпурный' : '#470736',
'очень глубокий красный' : '#4F0014',
'очень глубокий пурпурно-красный' : '#470027',
'очень глубокий пурпурный' : '#320B35',
'очень светло-пурпурный' : '#E3A9BE',
'очень светлый желто-зеленый' : '#C6DF90',
'очень светлый зеленовато-синий' : '#A3C6C0',
'очень светлый зеленый' : '#98C793',
'очень светлый пурпурно-синий' : '#BAACC7',
'очень светлый синевато-зеленый' : '#A0D6B4',
'очень светлый синий' : '#A6BDD7',
'очень светлый фиолетовый' : '#EEBEF1',
'очень темно-пурпурный' : '#230D21',
'очень темный алый' : '#560319',
'очень темный желто-зеленый' : '#132712',
'очень темный зеленовато-синий' : '#022027',
'очень темный зеленый' : '#16251C',
'очень темный красно-пурпурный' : '#270A1F',
'очень темный красный' : '#320A18',
'очень темный оливковый' : '#362C12',
'очень темный пурпурно-красный' : '#28071A',
'очень темный синевато-зеленый' : '#001D18',
'очень темный хаки' : '#4C3C18',
'очищенный миндаль' : '#FFEBCD',
'панг' : '#C7FCEC',
'папоротник крайола' : '#71BC78',
'папоротниково-зеленый' : '#3D642D',
'пастельно-бирюзовый' : '#7FB5B5',
'пастельно-желтый' : '#EFA94A',
'пастельно-зеленый' : '#77DD77',
'пастельно-оранжевый' : '#FF7514',
'пастельно-розовый' : '#FFD1DC',
'пастельно-синий' : '#5D9B9B',
'пастельно-фиолетовый' : '#A18594',
'патиново-зеленый' : '#316650',
'перекати-поле' : '#DEAA88',
'перламутрово-бежевый' : '#6A5D4D',
'перламутрово-ежевичный' : '#6C6874',
'перламутрово-зеленый' : '#1C542D',
'перламутрово-золотой' : '#705335',
'перламутрово-оранжевый' : '#C35831',
'перламутрово-розовый' : '#B44C43',
'перламутрово-рубиновый' : '#721422',
'перламутрово-фиолетовый' : '#8673A1',
'перламутровый горечавково-синий' : '#2A6478',
'перламутровый медный' : '#763C28',
'перламутровый мышино-серый' : '#898176',
'перламутровый ночной' : '#102C54',
'перламутровый опаловый' : '#193737',
'перламутровый светло-серый' : '#9C9C9C',
'перламутровый темно-серый' : '#828282',
'персидский зеленый' : '#00A693',
'персидский индиго' : '#32127A',
'персидский красный' : '#CC3333',
'персидский розовый' : '#FE28A2',
'персидский синий' : '#6600FF',
'персиковый' : '#FFE5B4',
'персиковый крайола' : '#FFCFAB',
'перу' : '#CD853F',
'песок пустыни' : '#EFCDB8',
'песочно-желтый' : '#C6A664',
'песочный' : '#FCDD76',
'песочный серо-коричневый' : '#967117',
'пигментный зеленый' : '#00A550',
'пихтовый зеленый' : '#31372B',
'пламенная маджента крайола' : '#F8173E',
'платиново-серый' : '#7F7679',
'побег папайи' : '#FFEFD5',
'полумрак крайола' : '#8A795D',
'полуночно-синий' : '#003366',
'полуночный синий крайола' : '#1A4876',
'полуночный черный' : '#191970',
'последний вздох жако' : '#FF9218',
'почти черный' : '#131313',
'призрачно-белый' : '#F8F8FF',
'пурпурная пицца' : '#FF00CC',
'пурпурно-белый' : '#FADBC8',
'пурпурно-красный' : '#75151E',
'пурпурно-серый' : '#88706B',
'пурпурно-синий' : '#20155E',
'пурпурно-фиолетовый' : '#4A192C',
'пурпурно-черный' : '#1B1116',
'пурпурное горное величие' : '#9D81BA',
'пурпурное сердце' : '#7442C8',
'пурпурный' : '#800080',
'пшеничный' : '#F5DEB3',
'пылкий красно-оранжевый' : '#F75E25',
'пылкий розовый' : '#FF7E93',
'пыльно-серый' : '#7D7F7D',
'пыльный голубой' : '#B0E0E6',
'пюсовый' : '#CC8899',
'радикальный красный' : '#FF496C',
'рапсово-желтый' : '#F3DA0B',
'резедово-зеленый' : '#587246',
'ржаво-коричневый' : '#B7410E',
'розовато-лиловый крайола' : '#EF98AA',
'розовато-серый' : '#C8A696',
'розовая гвоздика' : '#FFAACC',
'розовая долина' : '#AB4E52',
'розовая фуксия' : '#FF77FF',
'розово-золотой' : '#B76E79',
'розово-коричневый' : '#BC8F8F',
'розово-лавандовый' : '#FFF0F5',
'розово-серо-коричневый' : '#905D5D',
'розово-фиолетовый' : '#EE82EE',
'розово-эбонитовый' : '#674846',
'розовый' : '#FFC0CB',
'розовый (пощекочи меня)' : '#FC89AC',
'розовый антик' : '#D36E70',
'розовый кварц' : '#AA98A9',
'розовый лес' : '#65000B',
'розовый маунтбэттена' : '#997A8D',
'розовый поросенок' : '#FDDDE6',
'розовый фламинго' : '#FC74FD',
'розовый щербет' : '#F78FA7',
'рубиново-красный' : '#9B111E',
'румянец' : '#DE5D83',
'рыжий' : '#D77D31',
'салатовый' : '#99FF99',
'сангина' : '#92000A',
'сапфирово-синий' : '#1D1E33',
'сапфировый' : '#082567',
'светлая вишня' : '#DE3163',
'светлая мальва (светло-розовато-лиловый)' : '#DCD0FF',
'светлая сиена (почти чистый оранжевый)' : '#E28B00',
'светлая слива' : '#DDA0DD',
'светлая слоновая кость' : '#E6D690',
'светло-бирюзовый' : '#40E0D0',
'светло-вишневый крайола' : '#DD4492',
'светло-голубой' : '#87CEFA',
'светло-желтый' : '#FFFFE0',
'светло-желтый золотистый' : '#FAFAD2',
'светло-зеленый' : '#90EE90',
'светло-золотистый' : '#FFEC8B',
'светло-коралловый' : '#FFBCAD',
'светло-коричневый' : '#987654',
'светло-морковный' : '#ED9121',
'светло-оливковый' : '#846A20',
'светло-песочный' : '#FDEAA8',
'светло-пурпурный' : '#BA7FA2',
'светло-розовая фуксия' : '#F984EF',
'светло-розовый' : '#FFB6C1',
'светло-серебристый' : '#C9C0BB',
'светло-серый' : '#BBBBBB',
'светло-синий' : '#A6CAF0',
'светло-тициановый' : '#D84B20',
'светло-фиолетовый' : '#876C99',
'светлое зеленое море' : '#20B2AA',
'светлый аспидно-серый' : '#778899',
'светлый глубокий желтый' : '#FFD35F',
'светлый джинсовый' : '#2B6CC4',
'светлый желто-зеленый' : '#DCD36A',
'светлый желто-коричневый' : '#BB8B54',
'светлый желто-розовый' : '#FFB28B',
'светлый зеленовато-белый' : '#BAAF96',
'светлый зеленовато-желтый' : '#FFDE5A',
'светлый зеленовато-синий' : '#649A9E',
'светлый карминово-розовый' : '#E66761',
'светлый коричневато-серый' : '#8B6D5C',
'светлый коричневый' : '#A86540',
'светлый красно-коричневый' : '#AA6651',
'светлый красно-пурпурный' : '#BB6C8A',
'светлый малиново-красный' : '#E63244',
'светлый оливково-коричневый' : '#945D0B',
'светлый оливковый серый' : '#887359',
'светлый оранжевый' : '#FFA161',
'светлый пурпурно-розовый' : '#FFA8AF',
'светлый пурпурно-серый' : '#C8A99E',
'светлый пурпурно-синий' : '#837DA2',
'светлый розово-лиловый' : '#EA899A',
'светлый серо-желто-коричневый' : '#B48764',
'светлый серо-коричневый' : '#946B54',
'светлый серо-красно-коричневый' : '#966A57',
'светлый серо-красный' : '#B17267',
'светлый серо-оливковый' : '#8B734B',
'светлый серо-пурпурно-красный' : '#B27070',
'светлый серо-синий' : '#84C3BE',
'светлый серый' : '#D7D7D7',
'светлый сине-серый' : '#6C92AF',
'светлый синевато-зеленый' : '#669E85',
'светлый синевато-серый' : '#BEADA1',
'светлый синий' : '#ADD8E6',
'светлый стальной синий' : '#B0C4DE',
'светлый телегрей' : '#D0D0D0',
'светлый хаки' : '#F0E68C',
'светлый циан' : '#E0FFFF',
'селадон' : '#ACE1AF',
'сепия (каракатица)' : '#704214',
'сепия коричневый' : '#382C1E',
'сепия крайола' : '#A5694F',
'серая белка' : '#78858B',
'серая спаржа' : '#465945',
'серая умбра' : '#332F2C',
'серебристо-серый' : '#8A9597',
'серебряный' : '#C0C0C0',
'серебряный крайола' : '#CDC5C2',
'серо-бежевый' : '#9E9764',
'серобуромалиновый' : '#735184',
'серовато-желто-зеленый' : '#90845B',
'серовато-желто-коричневый' : '#785840',
'серовато-желто-розовый' : '#D39B85',
'серовато-желтый' : '#CEA262',
'серовато-зеленовато-желтый' : '#C4A55F',
'серовато-зеленый' : '#575E4E',
'серовато-коричневый' : '#5A3D30',
'серовато-красно-коричневый' : '#5E3830',
'серовато-красно-оранжевый' : '#B85D43',
'серовато-красно-пурпурный' : '#7D4D5D',
'серовато-красный' : '#8C4743',
'серовато-оливковый' : '#52442C',
'серовато-оранжевый' : '#C2A894',
'серовато-пурпурно-красный' : '#8C4852',
'серовато-пурпурно-розовый' : '#CC9293',
'серовато-пурпурно-синий' : '#413D51',
'серовато-пурпурный' : '#72525C',
'серовато-розовый' : '#CF9B8F',
'серовато-синий' : '#4A545C',
'серовато-фиолетовый' : '#46394B',
'сероватый оливково-зеленый' : '#48442D',
'серое окно' : '#9DA1AA',
'серый' : '#808080',
'серый бетон' : '#686C5E',
'серый зеленый чай' : '#CADABA',
'серый коричневый' : '#403A3A',
'серый крайола' : '#95918C',
'серый мох' : '#6C7059',
'серый нейтральный' : '#A0A0A4',
'серый оливковый' : '#3E3B32',
'серый синий' : '#26252D',
'серый хаки' : '#6A5F31',
'серый шелк' : '#CAC4B0',
'серый шифер  аспидно-серый' : '#708090',
'сигнальный желтый' : '#E5BE01',
'сигнальный зеленый' : '#317F43',
'сигнальный коричневый' : '#6C3B2A',
'сигнальный красный' : '#A52019',
'сигнальный оранжевый' : '#FF9900',
'сигнальный серый' : '#969992',
'сигнальный синий' : '#1E2460',
'сигнальный фиолетовый' : '#924E7D',
'сигнальный черный' : '#282828',
'сиена' : '#A0522D',
'сиена жженая' : '#E97451',
'сизый' : '#79A0C1',
'сине-зеленый' : '#1F3A3D',
'сине-зеленый крайола' : '#0D98BA',
'сине-лиловый' : '#8A2BE2',
'сине-серый крайола' : '#6699CC',
'сине-сиреневый' : '#6C4675',
'сине-фиолетовый крайола' : '#7366BD',
'синевато-белый' : '#F9DFCF',
'синевато-серый' : '#7D746D',
'синевато-черный' : '#151719',
'синий' : '#0000FF',
'синий-синий иней' : '#AFDAFC',
'синий градуса' : '#007DFF',
'синий клейна' : '#3A75C4',
'синий крайола' : '#1F75FE',
'синий серый' : '#474B4E',
'синий цвета яиц странствующего дрозда' : '#1FCECB',
'синий чирок' : '#18A7B5',
'синий экран смерти' : '#122FAA',
'синяя лазурь (лазурно-голубой)' : '#2A52BE',
'синяя пыль' : '#003399',
'синяя сталь' : '#4682B4',
'синяя элис' : '#F0F8FF',
'сиреневый' : '#C8A2C8',
'сияющая орхидея' : '#B565A7',
'скандальный оранжевый' : '#FF6E4A',
'скарлет' : '#FC2847',
'сладкая вата' : '#FFBCD9',
'сланцево-серый' : '#434750',
'сливовый' : '#660066',
'сливовый крайола' : '#8E4585',
'сливочно-кремовый' : '#F2DDC6',
'сливочный' : '#F2E8C9',
'слоновая кость' : '#FFFFF0',
'снежно-синий' : '#ACE5EE',
'солнечно-желтый' : '#F39F18',
'сомон' : '#EFAF8C',
'сосновый зеленый' : '#2C5545',
'сочный каштановый крайола' : '#B94E48',
'спаржа' : '#7BA05B',
'спаржа крайола' : '#87A96B',
'средний карминный' : '#AF4035',
'средний персидский синий' : '#0067A5',
'средний пурпурный' : '#9370D8',
'средний серый' : '#817066',
'стальной синий' : '#231A24',
'старинный розовый' : '#C08081',
'старое золото' : '#CFB53B',
'старое кружево' : '#FDF5E6',
'старый лен' : '#EEDC82',
'сырая охра' : '#D68A59',
'сырая умбра' : '#714B23',
'телегрей' : '#909090',
'телемагента' : '#CF3476',
'темная византия' : '#5D3954',
'темная орхидея' : '#9932CC',
'темно-алый' : '#CB2821',
'темно-бирюзовый' : '#116062',
'темно-голубой' : '#3B83BD',
'темно-грушевый' : '#D8A903',
'темно-желтый' : '#B07D2B',
'темно-зеленый' : '#013220',
'темно-каштановый' : '#986960',
'темно-коралловый' : '#CD5B45',
'темно-коричневый' : '#654321',
'темно-красный' : '#8B0000',
'темно-лазурный' : '#08457E',
'темно-лососевый' : '#E9967A',
'темно-мандариновый' : '#FFA812',
'темно-оливковый' : '#556832',
'темно-оранжевый' : '#FF8C00',
'темно-персиковый' : '#FFDAB9',
'темно-пурпурный' : '#472A3F',
'темно-розовый' : '#E75480',
'темно-серая мальва (розовато-лилово-серый)' : '#915F6D',
'темно-серо-коричневый' : '#483C32',
'темно-серый' : '#49423D',
'темно-синий' : '#002137',
'темно-синий (цвет формы морских офицеров)' : '#000080',
'темно-синий крайола' : '#1974D2',
'темно-фиолетовый' : '#9400D3',
'темное зеленое море' : '#8FBC8F',
'темный аспидно-синий' : '#483D8B',
'темный весенне-зеленый' : '#177245',
'темный желто-зеленый' : '#57A639',
'темный желто-коричневый' : '#918151',
'темный желто-розовый' : '#CC6C5C',
'темный желтовато-зеленый' : '#304B26',
'темный желтовато-коричневый' : '#3F2512',
'темный зеленовато-желто-зеленый' : '#313830',
'темный зеленовато-желтый' : '#9B8127',
'темный зеленовато-серый' : '#45433B',
'темный зеленовато-синий' : '#003841',
'темный зеленый' : '#203A27',
'темный зеленый чай' : '#BADBAD',
'темный золотарник (темно-золотой)' : '#B8860B',
'темный индиго' : '#310062',
'темный коричневый' : '#35170C',
'темный красно-коричневый' : '#321011',
'темный красно-оранжевый' : '#9B2F1F',
'темный красно-пурпурный' : '#4F273A',
'темный красно-серый' : '#523C36',
'темный красный' : '#681C23',
'темный маджента' : '#8B008B',
'темный мандарин' : '#EA7500',
'темный оливково-зеленый' : '#232C16',
'темный оливково-коричневый' : '#302112',
'темный оранжево-желтый' : '#C37629',
'темный пастельно-зеленый' : '#03C03C',
'темный пурпурно-красный' : '#5B1E31',
'темный пурпурно-розовый' : '#C76574',
'темный пурпурно-серый' : '#564042',
'темный пурпурно-синий' : '#1A162A',
'темный пурпурно-фиолетовый' : '#660099',
'темный розовый' : '#C76864',
'темный серо-желтый' : '#A47C45',
'темный серо-коричневый' : '#32221A',
'темный серо-красно-коричневый' : '#371F1C',
'темный серо-красный' : '#482A2A',
'темный серо-оливково-зеленый' : '#27261A',
'темный серо-оливковый' : '#2B2517',
'темный серо-синий' : '#2C3337',
'темный синевато-зеленый' : '#013A33',
'темный синевато-черный' : '#464544',
'темный телегрей' : '#82898F',
'темный терракотовый' : '#4E3B31',
'темный ультрамариновый' : '#00008B',
'темный хаки' : '#BDB76B',
'темный циан' : '#008B8B',
'темный черновато-пурпурный' : '#452D35',
'темный янтарь' : '#FF7E00',
'терракота' : '#CC4E5C',
'терракотовый' : '#904D30',
'тиффани' : '#0ABAB5',
'тихоокеанский синий' : '#1CA9C9',
'тициановый' : '#D53E07',
'томатно-красный' : '#A12312',
'томатный' : '#FF6347',
'травяной' : '#5DA130',
'травяной (очень темный лимонный зеленый)' : '#006400',
'травяной зеленый' : '#35682D',
'транспортно-желтый' : '#FAD201',
'транспортный зеленый' : '#308446',
'транспортный красный' : '#CC0605',
'транспортный оранжевый' : '#F54021',
'транспортный пурпурный' : '#A03472',
'транспортный серый' : '#8D948D',
'транспортный синий' : '#063971',
'транспортный черный' : '#1E1E1E',
'трилистник крайола' : '#45CEA2',
'тростниково-зеленый' : '#6C7156',
'турецкий розовый' : '#B57281',
'тускло-амарантово-розовый' : '#DDBEC3',
'тускло-розовый' : '#FFE4E1',
'тусклый мандарин' : '#F28500',
'тусклый пурпурный' : '#AE848B',
'тусклый серый' : '#696969',
'тыква (тыквенный)' : '#FF7518',
'ультрамариново-синий' : '#20214F',
'ультрамариновый' : '#120A8F',
'умбра жженая' : '#8A3324',
'умеренно-бирюзовый' : '#48D1CC',
'умеренно-зеленое море' : '#3CB371',
'умеренно-оливковый' : '#5E490F',
'умеренно-темный пурпурный' : '#803E75',
'умеренно зеленый' : '#C0DCC0',
'умеренный аквамариновый' : '#66CDAA',
'умеренный аспидно-синий' : '#7B68EE',
'умеренный весенний зеленый' : '#00FA9A',
'умеренный желто-зеленый' : '#8B8940',
'умеренный желто-коричневый' : '#7D512D',
'умеренный желто-розовый' : '#EE9374',
'умеренный желтовато-зеленый' : '#657F4B',
'умеренный желтый' : '#D79D41',
'умеренный зеленовато-желтый' : '#C4A43D',
'умеренный зеленовато-синий' : '#30626B',
'умеренный зеленый' : '#386646',
'умеренный коричневый' : '#673923',
'умеренный красно-оранжевый' : '#D35339',
'умеренный красно-пурпурный' : '#8C4566',
'умеренный красный' : '#AB343A',
'умеренный оливково-зеленый' : '#434B1B',
'умеренный оранжево-желтый' : '#F7943C',
'умеренный оранжевый' : '#E8793E',
'умеренный пурпурно-красный' : '#A73853',
'умеренный пурпурно-розовый' : '#E28090',
'умеренный пурпурно-синий' : '#423C63',
'умеренный пурпурный' : '#7F4870',
'умеренный розовый' : '#EE9086',
'умеренный серо-коричневый' : '#674C47',
'умеренный синевато-зеленый' : '#2F6556',
'умеренный синий' : '#395778',
'умеренный фиолетово-красный' : '#C71585',
'умеренный фиолетовый' : '#543964',
'умеренный цвет орхидеи' : '#BA55D3',
'фалунский красный' : '#801818',
'фанданго' : '#B55489',
'фельдграу' : '#4D5D53',
'фиалковый' : '#EA8DF7',
'фиолетово-баклажанный' : '#991199',
'фиолетово-красный крайола' : '#F75394',
'фиолетово-сизый' : '#8000FF',
'фиолетово-синий' : '#354D73',
'фиолетово-синий крайола' : '#324AB2',
'фиолетовый' : '#8B00FF',
'фиолетовый крайола (пурпурный)' : '#926EAE',
'фисташковый' : '#BEF574',
'французский розовый' : '#F64A8A',
'фталоцианиновый зеленый' : '#123524',
'фузи-вузи' : '#CC6666',
'фуксия (фуксин)' : '#F754E1',
'фуксия крайола' : '#C364C5',
'хаки' : '#806B2A',
'хромовый зеленый' : '#2E3A23',
'цвет блошиного брюшка' : '#4E1609',
'цвет вконтакте' : '#4D7198',
'цвет влюбленной жабы' : '#3CAA3C',
'цвет детской неожиданности' : '#F7F21A',
'цвет елки' : '#2A5C03',
'цвет желтого школьного автобуса' : '#FFD800',
'цвет загара (желто-коричневый)' : '#D2B48C',
'цвет загара крайола' : '#FAA76C',
'цвет красного моря' : '#1F4037',
'цвет маленького мандарина' : '#FFA474',
'цвет медвежьего ушка' : '#834D18',
'цвет мокрого асфальта' : '#505050',
'цвет морской волны (аква)' : '#008CF0',
'цвет морской раковины (морская пена)' : '#FFF5EE',
'цвет окраски птицы чирок (сине-зеленый)' : '#008080',
'цветочный белый' : '#FFFAF0',
'цвет пергидрольной блондинки' : '#EEE6A3',
'цвет пожарной машины' : '#CE2029',
'цвет слоновой кости (айвори)' : '#FFFDDF',
'цвет суеты' : '#E3256B',
'цвет твиттера' : '#1FAEE9',
'цвет фейсбука' : '#3B5998',
'цвет хабрахабра' : '#78A2B7',
'цвет черного моря' : '#1A4780',
'цвет шампанского' : '#FCFCEE',
'цвет шелковистых нитевидных пестиков початков неспелой кукурузы' : '#FFF8DC',
'цвет яйца дрозда' : '#00CCCC',
'цвет яндекса' : '#FFCC00',
'цементно-серый (цементный)' : '#7D8471',
'циан  цвет морской волны' : '#00FFFF',
'цинково-желтый' : '#F8F32B',
'циннвальдит' : '#EBC2AF',
'циннвальдитово-розовый' : '#FFCBBB',
'черно-зеленый' : '#343E40',
'черно-коричневый' : '#212121',
'черно-красный' : '#412227',
'черно-оливковый' : '#3B3C36',
'черно-серый' : '#23282B',
'черно-синий' : '#18171C',
'черновато-зеленый' : '#141613',
'черновато-красный' : '#1F0E11',
'черновато-пурпурный' : '#1D1018',
'черновато-синий' : '#161A1E',
'черный' : '#000000',
'черный янтарь' : '#0A0A0A',
'чертополох' : '#D8BFD8',
'чертополох крайола' : '#EBC7DF',
'шамуа' : '#A08040',
'шапка деда мороза' : '#CA3A27',
'шапка санта-клауса' : '#ED4830',
'шартрез  ядовито-зеленый' : '#7FFF00',
'шафраново-желтый' : '#F5D033',
'шафрановый' : '#F4C430',
'шелковица крайола' : '#C54B8C',
'шокирующий розовый крайола' : '#FB7EFD',
'шоколадно-коричневый' : '#45322E',
'шоколадный' : '#D2691E',
'экрю' : '#CDB891',
'экстравагантный розовый крайола' : '#FF33CC',
'электрик' : '#7DF9FF',
'электрик лайм (лаймовый)' : '#CCFF00',
'электрик лайм крайола' : '#CEFF1D',
'ядовито-зеленый' : '#40826D',
'янтарный' : '#FFBF00',
'яркий желто-зеленый' : '#93AA00',
'яркий желто-розовый' : '#FF845C',
'яркий зеленовато-желтый' : '#F4C800',
'яркий зеленый' : '#007D34',
'яркий красно-оранжевый' : '#F13A13',
'яркий красно-пурпурный' : '#7E0059',
'яркий красный' : '#C10020',
'яркий оранжево-желтый' : '#FF8E00',
'яркий оранжевый' : '#FF6800',
'яркий пурпурно-красный' : '#D5265B',
'яркий пурпурный' : '#943391',
'яркий синевато-зеленый' : '#00836E',
'яркий фиолетовый крайола' : '#8F509D',
'ярко-бирюзовый' : '#08E8DE',
'ярко-желтый' : '#FFB300',
'ярко-зеленый' : '#66FF00',
'ярко-мандариновый' : '#FFA089',
'ярко-розовый' : '#FC0FC0',
'ярко-синий' : '#007CAD',
'ярко-сиреневый' : '#E0B0FF',
'ярко-фиолетовый' : '#CD00CD'}


    def parse(self, text):
        text = [[self.morph.parse(word)[0].normal_form for word in line.split(' ')]
                for line in text.split(',')]
        main_part = []
        for line in text:
            main_part.append({'noun': 'none', 'adj': []})
            for word in line:
                if len(word) == 0:
                    continue
                if self.morph.parse(word)[0].tag.POS == 'NOUN':
                    main_part[-1]['noun'] = word
                else:
                    main_part[-1]['adj'].append(word)
        return main_part

    def get_color_by_name(self, color):
        if color in self.color_map.keys():
            return self.color_map[color]

    def get_all_colors(self, adj_list):
        ans = []
        for color in adj_list:
            if color in self.color_map.keys():
                ans.append(self.get_color_by_name(color))
        if len(ans) > 0:
            return ans[0]
        return '#000000'

    def get_real_synonymous(self, text):
        '''return reduced extract with noun that compare to models'''
        extract = self.parse(text)
        data = []
        for line in extract:
            noun = line['noun']
            if noun not in self.stored_names.keys():
                continue
            data.append({})
            data[-1]['model_path'] = self.stored_paths[noun]
            data[-1]['effects'] = {}
            data[-1]['effects']['color'] = self.get_all_colors(line['adj'])
            data[-1]['coordinate'] = (0, 0, 0)

        return json.dumps(data)
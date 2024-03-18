var simplemaps_europemap_mapdata={
  main_settings: {
    //General settings
		width: "responsive", //or 'responsive'
    height: 400,
    background_color: "#FFFFFF",
    background_transparent: "yes",
    popups: "detect",
    
		//State defaults
		state_description: "State description",
    state_color: "#88A4BC",
    state_hover_color: "#3B729F",
    state_url: "/map_of_wines",
    border_size: 1.5,
    border_color: "#ffffff",
    all_states_inactive: "no",
    all_states_zoomable: "no",
    
		//Location defaults
		location_description: "SHREK",
    location_color: "#FF0067",
    location_opacity: 0.8,
    location_hover_opacity: 1,
    location_url: "",
    location_size: 25,
    location_type: "square",
    location_border_color: "#FFFFFF",
    location_border: 2,
    location_hover_border: 2.5,
    all_locations_inactive: "no",
    all_locations_hidden: "no",
    
		//Label defaults
		label_color: "#ffffff",
    label_hover_color: "#ffffff",
    label_size: 22,
    label_font: "Arial",
    hide_labels: "no",
   
		//Zoom settings
		manual_zoom: "yes",
    back_image: "no",
    arrow_box: "no",
    navigation_size: "40",
    navigation_color: "#f7f7f7",
    navigation_border_color: "#636363",
    initial_back: "no",
    initial_zoom: -1,
    initial_zoom_solo: "no",
    region_opacity: 1,
    region_hover_opacity: 0.6,
    zoom_out_incrementally: "yes",
    zoom_percentage: 0.99,
    zoom_time: 0.5,
    
		//Popup settings
		popup_color: "white",
    popup_opacity: 0.9,
    popup_shadow: 1,
    popup_corners: 5,
    popup_font: "12px/1.5 Verdana, Arial, Helvetica, sans-serif",
    popup_nocss: "no",
    
		//Advanced settings
		div: "map",
    auto_load: "yes",
    rotate: "0",
    url_new_tab: "no",
    images_directory: "default",
    import_labels: "no",
    fade_time: 0.1,
    link_text: "View Website"
  },
  state_specific: {
    AD: {
      name: "Andorra",
      description: "Nestled in the Pyrenees, where ski slopes and duty-free shopping tempt visitors, and Catalan culture thrives in a mountainous paradise.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Andorra",
      state_url: "/map_of_wines/Andorra"
    },
    AL: {
      name: "Albania",
      description: "Where rugged mountains and pristine beaches hide ancient ruins and Byzantine churches, and the hospitality of the locals warms every visitor's heart.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Albania",
      state_url: "/map_of_wines/Albania"
      // state_url: "https://apple.com",
    },
    AM: {
      name: "Armenia",
      description: "Nestled in the Caucasus Mountains, where ancient monasteries cling to rugged cliffs and the spirit of resilience echoes through millennia of history.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Armenia",
      state_url: "/map_of_wines/Armenia"
    },
    AT: {
      name: "Austria",
      description: "Where the sound of Mozart floats through Baroque palaces, and the hills are alive with the taste of strudel and schnitzel.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Austria",
      state_url: "/map_of_wines/Armenia"
    },
    BA: {
      name: "Bosnia and Herzegovina",
      description: "Amidst Ottoman bridges and medieval towns, the scars of history are healed by the warmth of Bosnian hospitality and a shared love for coffee.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Bosnia and Herzegovina",
      state_url: "/map_of_wines/Bosnia and Herzegovina"
    },
    BE: {
      name: "Belgium",
      description: "Amidst medieval cities and rolling countryside, waffles and chocolate reign supreme in a land where every beer tells a story.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Belgium",
      state_url: "/map_of_wines/Belgium"
    },
    BG: {
      name: "Bulgaria",
      description: "In a land where ancient civilizations left their mark on majestic ruins, rose-scented valleys offer a glimpse into a rich cultural heritage.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Bulgaria",
      state_url: "/map_of_wines/Belgium"
    },
    BY: {
      name: "Belarus",
      description: "москалик",
      color: "bisque",
      hover_color: "default",
      url: "https://ssu.gov.ua/"
    },
    CH: {
      name: "Switzerland",
      description: "Where the pristine Alps guard secret chocolate recipes, and punctuality is as sacred as the shimmering lakes.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Switzerland",
      state_url: "/map_of_wines/Switzerland"
    },
    CY: {
      name: "Cyprus",
      description: "Where ancient ruins dot the coastline of a divided island, and the Mediterranean sun warms the hearts of visitors with Cypriot hospitality.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Cyprus",
      state_url: "/map_of_wines/Cyprus"
    },
    CZ: {
      name: "Czech Republic",
      description: "Where the spires of Prague pierce the sky, and beer flows as freely as the Vltava River.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Czech Republic",
      state_url: "/map_of_wines/Czech Republic"
    },
    DE: {
      name: "Germany",
      description: "Amongst the forests and fairytale castles, efficiency and precision dance hand in hand with a love for beer and bratwurst.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Germany",
      state_url: "/map_of_wines/Germany"
    },
    DK: {
      name: "Denmark",
      description: "Where cozy 'hygge' vibes warm even the coldest winters, and biking is more than just a mode of transportation — it's a way of life.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Denmark",
      state_url: "/map_of_wines/Denmark"
    },
    EE: {
      name: "Estonia",
      description: "Amidst medieval old towns and Baltic shores, a tech-savvy spirit mingles with timeless traditions under the Northern Lights.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Estonia",
      state_url: "/map_of_wines/Estonia"
    },
    ES: {
      name: "Spain",
      description: "Where the rhythm of flamenco echoes through the vibrant streets, and siestas are a sacred art form.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Spain",
      state_url: "/map_of_wines/Spain"
    },
    FI: {
      name: "Finland",
      description: "Amidst endless forests and lakes, saunas offer solace from the chill, and the midnight sun whispers tales of magic.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Finland",
      state_url: "/map_of_wines/Finland"
    },
    FR: {
      name: "France",
      description: "Where the aroma of freshly baked baguettes dances in the air, and every corner whispers tales of romance and revolution.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/France",
      state_url: "/map_of_wines/France",
    },
    GB: {
      name: "United Kingdom",
      description: "Where the rain-soaked landscapes are adorned with a quirky charm, and tea is the answer to every problem.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/United Kingdom",
      state_url: "/map_of_wines/United Kingdom"
    },
    GE: {
      name: "Georgia",
      description: "Where the mighty Caucasus meets the Black Sea, and the hospitality of the locals is as warm as the sun-drenched vineyards that blanket the hills.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Georgia",
      state_url: "/map_of_wines/Georgia"
    },
    GR: {
      name: "Greece",
      description: "In the land of gods and ancient ruins, the azure sea whispers secrets of mythology, while bouzouki melodies fill the tavernas.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Greece",
      state_url: "/map_of_wines/Greece"
    },
    HR: {
      name: "Croatia",
      description: "Where the Adriatic coastline sparkles with hidden coves and ancient cities, and the rhythm of Dalmatian music fills the sea-scented air.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Croatia",
      state_url: "/map_of_wines/Croatia"
    },
    HU: {
      name: "Hungary",
      description: "Amongst thermal baths and grandiose architecture, the Danube weaves tales of a nation rich in culture and paprika.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Hungary",
      state_url: "/map_of_wines/Hungary"
    },
    IE: {
      name: "Ireland",
      description: "In the land of leprechauns and rolling green hills, pubs are more than just drinking holes—they're storytelling sanctuaries.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Ireland",
      state_url: "/map_of_wines/Ireland"
    },
    IS: {
      name: "Iceland",
      description: "Where fire and ice collide in a land of volcanic landscapes and geothermal wonders, and tales of Norse mythology linger in the air.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Iceland",
      state_url: "/map_of_wines/Iceland"
    },
    IT: {
      name: "Italy",
      description: " A land where the sun-kissed vineyards hum melodies of passion, and every cobblestone street leads to a culinary adventure.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Italy",
      state_url: "/map_of_wines/Italy"
    },
    LI: {
      name: "Liechtenstein",
      description: "Where alpine landscapes and medieval castles create a fairy-tale setting, and a principality thrives as a haven of peace and prosperity.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Liechtenstein",
      state_url: "/map_of_wines/Liechtenstein"
    },
    LT: {
      name: "Lithuania",
      description: "Where medieval castles stand guard over amber-strewn shores, and the haunting melodies of ancient folk songs echo across the countryside.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Lithuania",
      state_url: "/map_of_wines/Lithuania"
    },
    LU: {
      name: "Luxembourg",
      description: "Amongst picturesque vineyards and fairy-tale castles, the Grand Duchy shines as a pocket-sized gem of prosperity and tranquility.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Luxembourg",
      state_url: "/map_of_wines/Luxembourg"
    },
    LV: {
      name: "Latvia",
      description: "In a land where dense forests meet sandy beaches, the spirit of the Hanseatic League still whispers through the cobbled streets of Riga.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Latvia",
      state_url: "/map_of_wines/Latvia"
    },
    MD: {
      name: "Moldova",
      description: "Amidst rolling vineyards and hidden monasteries, the spirit of winemaking flows through the heart of Europe's least-visited gem.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Moldova",
      state_url: "/map_of_wines/Moldova"
    },
    ME: {
      name: "Montenegro",
      description: "Where rugged mountains meet turquoise seas, and the echoes of Venetian and Ottoman empires linger in fortified coastal towns.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Montenegro",
      state_url: "/map_of_wines/Montenegro"
    },
    MK: {
      name: "Macedonia",
      description: "Amidst dramatic landscapes and Ottoman-era bazaars, the spirit of Alexander the Great still inspires a nation rich in history and hospitality.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Macedonia",
      state_url: "/map_of_wines/Macedonia"
    },
    NL: {
      name: "Netherlands",
      description: "Where windmills spin tales of a bygone era, and bicycles rule the charming canal-lined streets.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Netherlands",
      state_url: "/map_of_wines/Netherlands"
    },
    NO: {
      name: "Norway",
      description: "Where fjords carve through rugged landscapes, and the Northern Lights paint the sky with ethereal beauty.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Norway",
      state_url: "/map_of_wines/Norway"
    },
    PL: {
      name: "Poland",
      description: "In a land where history echoes through medieval cities and hearty pierogi warm the soul",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Poland",
      state_url: "/map_of_wines/Poland"
    },
    PT: {
      name: "Portugal",
      description: "In the land of melancholic fado, cobblestone alleys lead to hidden treasures and custard tarts sweeten the air.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Portugal",
      state_url: "/map_of_wines/Portugal"
    },
    RO: {
      name: "Romania",
      description: "Where the mist of Transylvania shrouds ancient castles in mystery, and the folklore of vampires dances with the rhythm of gypsy music.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Romania",
      state_url: "/map_of_wines/Romania"
    },
    RS: {
      name: "Serbia",
      description: "Where the Danube and Sava rivers converge, and lively kafanas reverberate with the sounds of traditional music and hearty laughter.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Serbia",
      state_url: "/map_of_wines/Serbia"
    },
    SE: {
      name: "Sweden",
      description: "Amidst the midnight sun and snowy landscapes, minimalist design meets a love for fika and hygge.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Sweden",
      state_url: "/map_of_wines/Sweden"
    },
    SI: {
      name: "Slovenia",
      description: "In the land of fairytale forests and emerald rivers, a passion for outdoor adventure meets a love for fine wine and culinary delights.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Slovenia",
      state_url: "/map_of_wines/Slovenia"
    },
    SK: {
      name: "Slovakia",
      description: "Amongst the Carpathian peaks and medieval towns, the heart of Europe beats with a blend of history and natural beauty.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Slovakia",
      state_url: "/map_of_wines/Slovakia"
    },
    TR: {
      name: "Turkey",
      description: "Where East meets West in a kaleidoscope of culture, from the bustling bazaars of Istanbul to the ancient ruins of Ephesus and the turquoise waters of the Mediterranean coast.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Turkey",
      state_url: "/map_of_wines/Turkey"
    },
    UA: {
      name: "Ukraine",
      description: "Львівське Різдвяне» - це темне пиво з карамельно - пряним ароматом і ноткою різдвяних спецій, яке вариться до зимових свят.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Ukraine",
      state_url: "/map_of_wines/Ukraine"
    },
    XK: {
      name: "Kosovo",
      description: "In a land of rugged beauty and resilience, where ancient traditions meet the spirit of youthful optimism and determination for a brighter future.",
      color: "default",
      hover_color: "default",
      url: "/map_of_wines/Kosovo",
      state_url: "/map_of_wines/Kosovo"
    }
  },
  // locations: {
  //   "0": {
  //     lat: 49.857,
  //     lng: 24.341,
  //     name: "UCU",
  //   }
  // },
  labels: {}
};

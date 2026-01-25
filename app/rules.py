# rules.py
import re

RULES = [
    {
        "term": "wheat",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Gluten-containing cereal; common allergen.",
    },
    {
        "term": "palm oil",
        "tags": ["environmental"],
        "severity": "high",
        "reason": "Often linked to deforestation risk unless sustainably sourced.",
    },
    {
        "term": "wheat flour",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Derived from wheat; gluten-containing allergen.",
    },
    {
        "term": "malted barley flour",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Derived from barley; gluten-containing cereal.",
    },
    {
        "term": "barley",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Gluten-containing cereal.",
    },
    {
        "term": "soybean oil",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Derived from soy, a common allergen.",
    },
    {
        "term": "soy",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Common allergen.",
    },
    {
        "term": "milk",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Common dairy allergen.",
    },
    {
        "term": "eggs",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Common allergen.",
    },
    {
        "term": "tree nuts",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Common allergen group.",
    },
    {
        "term": "honey powder",
        "tags": ["vegan"],
        "severity": "low",
        "reason": "Bee-derived ingredient; avoided by many vegans.",
    },
    {
        "term": "honey",
        "tags": ["vegan"],
        "severity": "low",
        "reason": "Bee-derived ingredient; avoided by many vegans.",
    },
    {
        "term": "natural flavor",
        "tags": ["vegan"],
        "severity": "low",
        "reason": "Source may be plant or animal-derived; not always vegan.",
    },
    {
        "term": "palm oil",
        "tags": ["environmental"],
        "severity": "high",
        "reason": "Often linked to deforestation risk unless sustainably sourced.",
    },
    {
        "term": "soybean oil",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Derived from soy, a common allergen.",
    },
    {
        "term": "soy",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Common allergen.",
    },
    {
        "term": "soy lecithin",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Soy-derived emulsifier; common allergen.",
    },
    {
        "term": "milk",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Common dairy allergen.",
    },
    {
        "term": "nonfat milk",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Milk-derived ingredient; common allergen.",
    },
    {
        "term": "whey",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Milk-derived protein; common allergen.",
    },
    {
        "term": "caseinate",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Milk-derived protein; dairy allergen.",
    },
    {
        "term": "egg",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Common allergen.",
    },
    {
        "term": "wheat",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Gluten-containing cereal; common allergen.",
    },
    {
        "term": "wheat flour",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Derived from wheat; gluten-containing allergen.",
    },
    {
        "term": "barley",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Gluten-containing cereal.",
    },
    {
        "term": "malted barley flour",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Derived from barley; gluten-containing cereal.",
    },
    {
        "term": "tree nuts",
        "tags": ["allergens"],
        "severity": "high",
        "reason": "Common allergen group.",
    },
    {
        "term": "gelatin",
        "tags": ["vegan"],
        "severity": "high",
        "reason": "Typically derived from animal collagen.",
    },
    {
        "term": "honey",
        "tags": ["vegan"],
        "severity": "low",
        "reason": "Bee-derived ingredient; avoided by many vegans.",
    },
    {
        "term": "honey powder",
        "tags": ["vegan"],
        "severity": "low",
        "reason": "Bee-derived ingredient; avoided by many vegans.",
    },
    {
        "term": "cocoa",
        "tags": ["labor"],
        "severity": "med",
        "reason": "Labor-risk supply chains in some regions unless certified.",
    },
    {
        "term": "high fructose corn syrup",
        "tags": ["environmental"],
        "severity": "low",
        "reason": "Industrial sweetener associated with intensive corn agriculture.",
    },
    {
        "term": "corn syrup",
        "tags": ["environmental"],
        "severity": "low",
        "reason": "Industrial sweetener associated with intensive corn agriculture.",
    },
    {
        "term": "dextrose",
        "tags": ["environmental"],
        "severity": "low",
        "reason": "Refined sugar derived from corn processing.",
    },
    {
        "term": "partially hydrogenated soybean oil",
        "tags": ["environmental"],
        "severity": "med",
        "reason": "Highly processed oil with environmental and processing concerns.",
    },
    {
        "term": "natural flavor",
        "tags": ["vegan"],
        "severity": "low",
        "reason": "Source may be plant or animal-derived; not always vegan.",
    },
    {
        "term": "artificial flavor",
        "tags": ["vegan"],
        "severity": "low",
        "reason": "Synthetic flavoring; vegan status varies by formulation.",
    },
{ "term": "Red 3", "tags": ["neurotoxins", "behavioral"], "severity": "high", "reason": "Linked to thyroid tumors in animal studies; banned in cosmetics but allowed in food." },
    { "term": "Red 40", "tags": ["neurotoxins", "behavioral"], "severity": "high", "reason": "Petroleum-derived; linked to hyperactivity and ADHD in children." },
    { "term": "Yellow 5", "tags": ["neurotoxins", "behavioral"], "severity": "high", "reason": "Tartrazine; known to trigger hyperactivity and severe allergic reactions." },
    { "term": "Yellow 6", "tags": ["neurotoxins", "behavioral"], "severity": "high", "reason": "Sunset Yellow; associated with adrenal tumors and hypersensitivity." },
    { "term": "Blue 1", "tags": ["neurotoxins", "behavioral"], "severity": "medium", "reason": "Brilliant Blue; crosses the blood-brain barrier; potential neurotoxicity." },
    { "term": "Blue 2", "tags": ["neurotoxins", "behavioral"], "severity": "medium", "reason": "Indigo Carmine; linked to brain tumors in animal testing." },
    { "term": "Green 3", "tags": ["neurotoxins", "behavioral"], "severity": "medium", "reason": "Fast Green; linked to bladder and testes tumors in male rats." },
    { "term": "Orange B", "tags": ["neurotoxins", "behavioral"], "severity": "high", "reason": "Restricted use; high doses show toxicity to the liver and bile duct." },
    { "term": "Caramel Color III", "tags": ["carcinogens"], "severity": "medium", "reason": "Contains 4-MEI, a byproduct classified as a possible human carcinogen." },
    { "term": "Caramel Color IV", "tags": ["carcinogens"], "severity": "high", "reason": "Contains high levels of 4-MEI; requires a warning label in some jurisdictions (Prop 65)." },
    { "term": "Titanium Dioxide", "tags": ["carcinogens", "genotoxicity"], "severity": "high", "reason": "Banned in the EU; concerns regarding DNA damage and accumulation in the body." },
    { "term": "Citrus Red No. 2", "tags": ["carcinogens"], "severity": "high", "reason": "Used only on orange peels; proven to be carcinogenic in high doses." },
    { "term": "Aspartame", "tags": ["metabolic disruptors", "carcinogens"], "severity": "high", "reason": "Categorized as possibly carcinogenic (IARC); linked to headaches and dizziness." },
    { "term": "Acesulfame Potassium", "tags": ["carcinogens"], "severity": "medium", "reason": "Also known as Ace-K; contains methylene chloride, a known carcinogen." },
    { "term": "Saccharin", "tags": ["carcinogens"], "severity": "medium", "reason": "Historically linked to bladder cancer; avoided due to long-term safety concerns." },
    { "term": "Sucralose", "tags": ["digestive irritants", "metabolic disruptors"], "severity": "medium", "reason": "May negatively impact gut microbiome and reduce insulin sensitivity." },
    { "term": "High Fructose Corn Syrup", "tags": ["metabolic disruptors"], "severity": "high", "reason": "Highly processed; major driver of obesity, fatty liver, and Type 2 diabetes." },
    { "term": "Sodium Benzoate", "tags": ["carcinogens"], "severity": "high", "reason": "Can react with Vitamin C to form Benzene, a known human carcinogen." },
    { "term": "Potassium Sorbate", "tags": ["digestive irritants"], "severity": "low", "reason": "Can cause skin and respiratory irritation in sensitive individuals." },
    { "term": "BHA", "tags": ["carcinogens", "endocrine disruptors"], "severity": "high", "reason": "Butylated Hydroxyanisole; anticipated human carcinogen and hormone disruptor." },
    { "term": "BHT", "tags": ["endocrine disruptors"], "severity": "high", "reason": "Butylated Hydroxytoluene; linked to hormone disruption and liver toxicity." },
    { "term": "Sodium Nitrate", "tags": ["carcinogens"], "severity": "high", "reason": "Converts to nitrosamines in the stomach, which are highly carcinogenic." },
    { "term": "Sodium Nitrite", "tags": ["carcinogens"], "severity": "high", "reason": "Used in processed meats; strong link to colorectal cancer." },
    { "term": "Sulfur Dioxide", "tags": ["digestive irritants"], "severity": "medium", "reason": "Sulfite that can trigger severe asthma attacks and allergic reactions." },
    { "term": "Sodium Bisulfite", "tags": ["digestive irritants"], "severity": "medium", "reason": "Common sulfite used in wine/dried fruit; can cause respiratory distress." },
    { "term": "Propylparaben", "tags": ["endocrine disruptors"], "severity": "high", "reason": "Mimics estrogen; linked to decreased fertility and hormone imbalance." },
    { "term": "TBHQ", "tags": ["carcinogens"], "severity": "high", "reason": "Tert-Butylhydroquinone; linked to vision disturbances and liver enlargement." },
    { "term": "Potassium Bromate", "tags": ["carcinogens"], "severity": "high", "reason": "Dough conditioner banned in most countries; known human carcinogen." },
    { "term": "Azodicarbonamide", "tags": ["neurotoxins", "behavioral"], "severity": "medium", "reason": "The 'yoga mat chemical'; linked to respiratory issues and asthma." },
    { "term": "Carrageenan", "tags": ["digestive irritants"], "severity": "medium", "reason": "Seaweed derivative linked to gut inflammation, bloating, and IBS." },
    { "term": "Brominated Vegetable Oil", "tags": ["neurotoxins", "behavioral"], "severity": "high", "reason": "BVO; accumulates in body fat and can cause neurological damage." },
    { "term": "Partially Hydrogenated Oil", "tags": ["metabolic disruptors"], "severity": "high", "reason": "Source of Trans Fats; raises bad cholesterol (LDL) and damages heart health." },
    { "term": "Polysorbate 80", "tags": ["digestive irritants"], "severity": "medium", "reason": "Emulsifier that may disrupt the gut barrier and promote leaky gut." },
    { "term": "Monosodium Glutamate", "tags": ["neurotoxins", "behavioral"], "severity": "medium", "reason": "MSG; causes headaches and numbness in sensitive individuals." },
    { "term": "Disodium Inosinate", "tags": ["digestive irritants"], "severity": "low", "reason": "Flavor enhancer often used with MSG; can trigger issues for those with gout." }, 
]



def _norm(s: str) -> str:
    # lowercase, remove punctuation, collapse whitespace
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)   # keep letters/numbers/spaces
    s = re.sub(r"\s+", " ", s).strip()
    return s

def detect_flags(text: str, values: dict):
    enabled_tags = [k for k, v in (values or {}).items() if v]

    text_norm = _norm(text)

    results = []
    seen = set()

    for rule in RULES:
        if not any(tag in enabled_tags for tag in rule["tags"]):
            continue

        term = rule["term"]
        term_norm = _norm(term)

        # match as a whole word/phrase (avoids matching inside other words)
        pattern = r"\b" + re.escape(term_norm) + r"\b"

        if re.search(pattern, text_norm) and term not in seen:
            results.append(rule)
            seen.add(term)

        # plural fallback (egg <-> eggs, nut <-> nuts) without changing RULES
        if term_norm.endswith("s") is False:
            pattern_plural = r"\b" + re.escape(term_norm + "s") + r"\b"
            if re.search(pattern_plural, text_norm) and term not in seen:
                results.append(rule)
                seen.add(term)

    return results
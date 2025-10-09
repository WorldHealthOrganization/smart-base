# JSON Examples: Top 3 Options for DAK Component References

## Option 6: Extend Source Pattern (Recommended)

### Example dak.json
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  "name": "ANC",
  "title": "Antenatal Care",
  "version": "1.0.0",
  "status": "active",
  
  "indicators": [
    {
      "id": "ANCIND01",
      "name": "ANC contact coverage",
      "definition": "Percentage of pregnant women who attended at least one ANC contact",
      "numerator": "Number of pregnant women who attended ANC at least once",
      "denominator": "Total number of pregnant women",
      "disaggregation": "By age group, location"
    },
    {
      "id": "ANCIND02",
      "source": "http://who.int/indicators/ANC-IND-02.json"
    },
    {
      "id": "ANCIND03", 
      "source": "../shared-indicators/nutrition-indicator.json"
    }
  ],
  
  "decisionLogic": [
    {
      "id": "ANCDL01",
      "description": "Iron and folic acid supplementation decision",
      "source": "input/dmn/ANC.DT.IFA.dmn"
    },
    {
      "id": "ANCDL02",
      "source": "http://who.int/logic/ANC-DL-02.json"
    }
  ],
  
  "personas": [
    {
      "id": "P01",
      "title": "Community Health Worker",
      "description": "Provides basic ANC services at community level",
      "iscoCode": ["3253"]
    },
    {
      "id": "P02",
      "source": "http://who.int/personas/midwife.json"
    }
  ]
}
```

### Pros
- ✅ Consistent with existing `source` fields in DecisionSupportLogic/BusinessProcessWorkflow
- ✅ Single field name across all components
- ✅ Natural evolution of current design
- ✅ No changes to DAK.fsh structure

### Cons
- ⚠️ Overloading `source` with multiple meanings (DMN/BPMN files vs component instances)
- ⚠️ Need clear documentation on what URLs should return

---

## Option 5: New Reference Field (Alternative)

### Example dak.json
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  "name": "ANC",
  "title": "Antenatal Care",
  "version": "1.0.0",
  "status": "active",
  
  "indicators": [
    {
      "id": "ANCIND01",
      "name": "ANC contact coverage",
      "definition": "Percentage of pregnant women who attended at least one ANC contact",
      "numerator": "Number of pregnant women who attended ANC at least once",
      "denominator": "Total number of pregnant women",
      "disaggregation": "By age group, location"
    },
    {
      "id": "ANCIND02",
      "reference": "http://who.int/indicators/ANC-IND-02.json"
    },
    {
      "id": "ANCIND03",
      "reference": "../shared-indicators/nutrition-indicator.json"
    }
  ],
  
  "decisionLogic": [
    {
      "id": "ANCDL01",
      "description": "Iron and folic acid supplementation decision",
      "source": "input/dmn/ANC.DT.IFA.dmn"
    },
    {
      "id": "ANCDL02",
      "source": "input/dmn/ANC.DT.IPTp.dmn",
      "reference": "http://who.int/logic/ANC-DL-02.json"
    }
  ],
  
  "personas": [
    {
      "id": "P01",
      "title": "Community Health Worker",
      "description": "Provides basic ANC services at community level",
      "iscoCode": ["3253"]
    },
    {
      "id": "P02",
      "reference": "http://who.int/personas/midwife.json"
    }
  ]
}
```

### Pros
- ✅ Clear semantic distinction: `source` = process files, `reference` = component instances
- ✅ No confusion about what type of content the URL should return
- ✅ Can coexist with `source` field (as shown in ANCDL02)
- ✅ No changes to DAK.fsh structure

### Cons
- ⚠️ Requires adding field to all 9 component models
- ⚠️ Slight duplication vs Option 6

---

## Option 4: Separate Arrays (Alternative)

### Example dak.json
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  "name": "ANC",
  "title": "Antenatal Care",
  "version": "1.0.0",
  "status": "active",
  
  "indicators": [
    {
      "id": "ANCIND01",
      "name": "ANC contact coverage",
      "definition": "Percentage of pregnant women who attended at least one ANC contact",
      "numerator": "Number of pregnant women who attended ANC at least once",
      "denominator": "Total number of pregnant women",
      "disaggregation": "By age group, location"
    }
  ],
  "indicatorsRef": [
    "http://who.int/indicators/ANC-IND-02.json",
    "../shared-indicators/nutrition-indicator.json"
  ],
  
  "decisionLogic": [
    {
      "id": "ANCDL01",
      "description": "Iron and folic acid supplementation decision",
      "source": "input/dmn/ANC.DT.IFA.dmn"
    }
  ],
  "decisionLogicRef": [
    "http://who.int/logic/ANC-DL-02.json"
  ],
  
  "personas": [
    {
      "id": "P01",
      "title": "Community Health Worker",
      "description": "Provides basic ANC services at community level",
      "iscoCode": ["3253"]
    }
  ],
  "personasRef": [
    "http://who.int/personas/midwife.json"
  ]
}
```

### Pros
- ✅ Maximum explicitness: inline vs referenced are clearly separated
- ✅ Simplest to process: just check two arrays
- ✅ No semantic overloading
- ✅ Arrays contain uniform types (objects vs URLs)

### Cons
- ⚠️ Doubles the number of fields in DAK structure (18 instead of 9)
- ⚠️ More verbose
- ⚠️ Could lead to questions about which array to use

---

## Processing Comparison

### Fetching All Indicators (Pseudocode)

**Option 6 & 5:**
```javascript
async function getAllIndicators(dak) {
  const indicators = [];
  
  for (const indicator of dak.indicators) {
    if (indicator.source || indicator.reference) {
      // Fetch from URL
      const external = await fetch(indicator.source || indicator.reference);
      indicators.push(external);
    } else {
      // Use inline data
      indicators.push(indicator);
    }
  }
  
  return indicators;
}
```

**Option 4:**
```javascript
async function getAllIndicators(dak) {
  const indicators = [];
  
  // Add inline indicators
  indicators.push(...dak.indicators);
  
  // Fetch referenced indicators
  for (const url of dak.indicatorsRef || []) {
    const external = await fetch(url);
    indicators.push(external);
  }
  
  return indicators;
}
```

**Analysis:**
- Option 4 is slightly simpler (no conditional logic per item)
- Options 5/6 keep related data together conceptually
- All three are easy to implement

---

## Validation Scenarios

### Scenario 1: Incomplete Referenced Instance
**Problem**: Referenced URL returns instance missing required fields

**Option 6/5 Handling:**
```javascript
if (indicator.source || indicator.reference) {
  // Inline data (like id, name) can provide metadata
  // Full data comes from URL
  metadata = {id: indicator.id, name: indicator.name};
  fullData = await fetch(indicator.source || indicator.reference);
  merged = {...metadata, ...fullData};
}
```

**Option 4 Handling:**
```javascript
// URL in indicatorsRef must return complete instance
// No inline metadata available
fullData = await fetch(url);
```

**Winner**: Options 5/6 allow hybrid approach with metadata inline

### Scenario 2: Checking What's Referenced
**Question**: "Show me all externally referenced components"

**Option 6/5:**
```javascript
const referenced = dak.indicators
  .filter(i => i.source || i.reference)
  .map(i => i.source || i.reference);
```

**Option 4:**
```javascript
const referenced = dak.indicatorsRef || [];
```

**Winner**: Option 4 slightly simpler

---

## Migration from Current State

### Current dak.json
```json
{
  "indicators": [
    {"id": "IND01", "name": "Coverage", ...}
  ]
}
```

### Option 6 Migration (Adding References)
```json
{
  "indicators": [
    {"id": "IND01", "name": "Coverage", ...},
    {"id": "IND02", "source": "http://..."}  // ADD
  ]
}
```
**Impact**: ✅ Backward compatible, existing instances unchanged

### Option 5 Migration (Adding References)
```json
{
  "indicators": [
    {"id": "IND01", "name": "Coverage", ...},
    {"id": "IND02", "reference": "http://..."}  // ADD
  ]
}
```
**Impact**: ✅ Backward compatible, existing instances unchanged

### Option 4 Migration (Adding References)
```json
{
  "indicators": [
    {"id": "IND01", "name": "Coverage", ...}
  ],
  "indicatorsRef": ["http://..."]  // ADD NEW FIELD
}
```
**Impact**: ✅ Backward compatible, existing instances unchanged

**All options are backward compatible!**

---

## Recommendation

**For most use cases: Choose Option 6 (Extend Source Pattern)**
- Builds on existing architecture
- Minimal changes required
- Natural evolution of current design

**If semantic clarity is critical: Choose Option 5 (New Reference Field)**
- Clearer distinction between process files and instances
- Can coexist with source field when needed

**If processing simplicity is paramount: Choose Option 4 (Separate Arrays)**
- Explicit separation of concerns
- Simplest iteration logic

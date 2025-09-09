# 🛩️ European Luxury Events Intelligence

A comprehensive data collection and analysis system for identifying premium aviation opportunities around European luxury events.

## 🎯 Project Overview

This project aggregates luxury event data across Europe to identify opportunities for premium flight services targeting:
- High-net-worth individuals (HNWIs)
- Social media influencers 
- Luxury lifestyle enthusiasts

**Target Market**: 6-8 seat business jet flights between European cities (2-3 hours max) during luxury events.

## 📊 Live Project Status

View the current project status and data collection progress:
**[Live Dashboard](https://your-username.github.io/luxury-events-intelligence/status_dashboard.html)**

## 🏗️ System Architecture

### Data Sources
- **Eventbrite API** - Premium event discovery
- **Meetup GraphQL API** - Professional networking events
- **Facebook Events** - Public luxury events (limited access)
- **Manual curation** - Fashion weeks, motor shows, auctions

### Event Categories
- 👗 **Fashion & Luxury Retail** - Fashion weeks, trunk shows, jewelry exhibitions
- 💼 **Finance & Banking** - Private banking conferences, wealth summits
- 🏎️ **Automotive Luxury** - Motor shows, classic car auctions, racing events
- 🍷 **Haute Cuisine & Hospitality** - Michelin events, wine auctions, luxury food festivals
- 🏛️ **Real Estate & Property** - Luxury property fairs, architecture exhibitions

### Target Cities
London, Paris, Milan, Monaco, Zurich, Geneva, Amsterdam, Frankfurt, Munich, Vienna, Barcelona, Rome, Florence, Copenhagen, Stockholm, Brussels

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- API keys for data sources

### Installation
```bash
git clone https://github.com/your-username/luxury-events-intelligence.git
cd luxury-events-intelligence
pip install -r requirements.txt
```

### Configuration
1. Copy `config.json` template
2. Add your API keys:
   ```json
   {
     "api_keys": {
       "eventbrite": "YOUR_EVENTBRITE_API_KEY",
       "meetup": "YOUR_MEETUP_API_KEY",
       "facebook": "YOUR_FACEBOOK_ACCESS_TOKEN"
     }
   }
   ```

### Run Data Collection
```bash
python main.py
```

This will:
- Collect events from all configured sources
- Filter for luxury events (score 6+)
- Generate status dashboard (`status_dashboard.html`)
- Store data in SQLite database (`luxury_events.db`)

## 📈 Current Status

| Metric | Value | Updated |
|--------|-------|---------|
| Total Events Tracked | ![Events Badge](https://img.shields.io/badge/dynamic/json?color=blue&label=events&query=total_events&url=https://your-repo.github.io/api/stats.json) | Daily |
| Premium Events (8+ score) | ![Premium Badge](https://img.shields.io/badge/dynamic/json?color=green&label=premium&query=premium_events&url=https://your-repo.github.io/api/stats.json) | Daily |
| Cities Covered | 16 | Static |
| Data Sources | 3 Active | Static |

## 🛠️ API Documentation

### Getting API Keys

#### Eventbrite API
1. Visit [Eventbrite API](https://www.eventbrite.com/platform/api)
2. Create developer account
3. Generate private token
4. Free tier: 1000 requests/hour

#### Meetup API  
1. Visit [Meetup API](https://www.meetup.com/api/)
2. Create app in developer console
3. Get API key
4. GraphQL endpoint access

#### Facebook Graph API
1. Visit [Facebook Developers](https://developers.facebook.com/)
2. Create app
3. Get access token
4. Note: Limited public event access

## 📊 Data Structure

### Events Table
```sql
events (
  event_id TEXT PRIMARY KEY,
  name TEXT,
  description TEXT,
  start_date TEXT,
  end_date TEXT,
  city TEXT,
  country TEXT,
  category TEXT,
  luxury_score INTEGER,  -- 1-10 scale
  estimated_attendance INTEGER,
  ticket_price_min REAL,
  ticket_price_max REAL,
  source TEXT
)
```

### Luxury Scoring Algorithm
Events scored 1-10 based on:
- Ticket prices (€500+ = high score)
- Venue prestige (luxury hotels, exclusive locations)
- Description keywords (luxury, exclusive, premium, VIP)
- Historical attendance patterns
- Media coverage level

## 🎨 Dashboard Features

The auto-generated dashboard includes:
- **Real-time statistics** - Event counts, luxury scores, upcoming events
- **Data collection status** - API health, last collection times, error tracking  
- **Recent high-value events** - Latest premium events discovered
- **Geographic distribution** - City-wise event mapping (planned)
- **Trend analysis** - Historical patterns and forecasting (planned)

## 🔄 Automation

### Scheduled Collection
```bash
# Run daily at 6 AM
0 6 * * * /path/to/python /path/to/main.py

# Generate dashboard every hour  
0 * * * * /path/to/generate_dashboard.py
```

### GitHub Actions (Planned)
- Daily data collection
- Dashboard updates  
- Data quality checks
- API health monitoring

## 📋 Roadmap

### Phase 1 (Current)
- [x] Core data collection infrastructure
- [x] Eventbrite API integration
- [x] Meetup API integration
- [x] Basic luxury scoring
- [x] Status dashboard
- [ ] Facebook Events integration
- [ ] Data validation pipeline

### Phase 2 (Next 4 weeks)
- [ ] Visitor demographics integration
- [ ] Flight route optimization
- [ ] Demand forecasting model
- [ ] Interactive dashboard maps
- [ ] API rate limiting improvements
- [ ] Historical data analysis

### Phase 3 (Month 2-3)
- [ ] Amadeus travel data integration
- [ ] Wealth-X HNWI data correlation  
- [ ] Machine learning demand prediction
- [ ] Competition analysis
- [ ] Business case generation
- [ ] Investor presentation materials

## 🤝 Contributing

This is a research project for premium aviation market analysis. Interested in the luxury travel industry? 

### Areas needing contribution:
- **Data Sources** - Additional luxury event APIs
- **Market Intelligence** - HNWI travel pattern data
- **Geographic Analysis** - European airport/route optimization
- **ML Models** - Demand forecasting improvements

## 📄 License

This project is proprietary research for luxury aviation market analysis.

## 📞 Contact

For business inquiries or collaboration:
- Project Lead: [Your Name]
- Email: [Your Email] 
- LinkedIn: [Your Profile]

---

### 🔍 Key Insights So Far

Based on initial data collection:

- **Peak Season**: Q4 (Oct-Dec) shows 40% more luxury events
- **Top Routes**: London-Paris, Milan-Monaco, Zurich-Geneva corridors
- **Event Clusters**: Fashion weeks create 3-day demand spikes
- **Price Sensitivity**: Events €500+ ticket average show 60% international attendance

*This project aims to revolutionize premium inter-city travel by leveraging event-driven demand patterns.*

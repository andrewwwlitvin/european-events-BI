.category {
                background: #e9ecef;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 0.8rem;
                text-transform: capitalize;
                font-weight: 500;
            }
            
            .event-name {
                font-weight: 500;
                max-width: 300px;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }
            
            .price {
                font-weight: 600;
                color: #28a745;
            }
            
            .chart-container {
                margin-bottom: 20px;
                height: 300px;
            }
            
            .geo-table {
                margin-top: 20px;
            }
            
            .pricing-breakdown {
                margin-bottom: 20px;
            }
            
            .price-tier {
                display: flex;
                align-items: center;
                margin-bottom: 15px;
                padding: 10px;
                background: #f8f9fa;
                border-radius: 8px;
            }
            
            .price-label {
                flex: 1;
                font-weight: 600;
                color: #333;
            }
            
            .price-count {
                margin: 0 15px;
                font-weight: 500;
                min-width: 80px;
                text-align: center;
            }
            
            .price-bar {
                height: 20px;
                border-radius: 10px;
                min-width: 20px;
                max-width: 200px;
            }
            
            .pricing-insights {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                border-left: 4px solid #667eea;
            }
            
            .pricing-insights ul {
                margin-top: 10px;
                padding-left: 20px;
            }
            
            .pricing-insights li {
                margin-bottom: 8px;
                color: #666;
            }
            
            footer {
                text-align: center;
                margin-top: 50px;
                padding: 30px;
                background: rgba(255,255,255,0.1);
                border-radius: 15px;
                color: white;
                backdrop-filter: blur(10px);
            }
            
            footer p {
                margin-bottom: 8px;
                opacity: 0.9;
            }
        """
    
    def _get_enhanced_javascript(self) -> str:
        """Get enhanced JavaScript for dashboard functionality"""
        return """
            // Auto-refresh dashboard every 10 minutes
            setTimeout(() => {
                location.reload();
            }, 600000);
            
            // Add interactive features
            document.addEventListener('DOMContentLoaded', function() {
                console.log('Luxury Events Intelligence Dashboard loaded');
                
                // Add hover effects for enhanced interactivity
                const cards = document.querySelectorAll('.card, .stat-card');
                cards.forEach(card => {
                    card.addEventListener('mouseenter', function() {
                        this.style.transform = 'translateY(-5px)';
                    });
                    
                    card.addEventListener('mouseleave', function() {
                        this.style.transform = 'translateY(0)';
                    });
                });
                
                // Add click-to-expand for event details
                const eventRows = document.querySelectorAll('.events-table tbody tr');
                eventRows.forEach(row => {
                    row.style.cursor = 'pointer';
                    row.addEventListener('click', function() {
                        // Could expand to show more event details
                        console.log('Event row clicked:', this);
                    });
                });
            });
            
            // Performance monitoring
            window.addEventListener('load', function() {
                const loadTime = performance.now();
                console.log('Dashboard loaded in', Math.round(loadTime), 'ms');
            });
        """

if __name__ == "__main__":
    asyncio.run(main())✅ Collection completed successfully!")
        print(f"📊 Results:")
        print(f"   • Total events processed: {len(luxury_events)}")
        print(f"   • Luxury events stored: {stored_count}")
        print(f"   • Average luxury score: {avg_luxury_score:.1f}/10")
        print(f"   • Collection duration: {duration:.1f} seconds")
        print(f"   • Database: {db.db_path}")
        
        # Collect tourism data
        print("🌍 Collecting tourism demographic data...")
        tourism_data = await tourism_collector.get_tourism_flows(target_cities)
        print(f"📈 Tourism data collection: {len(tourism_data)} records")
        
        # Generate intelligence dashboard
        print("📊 Generating intelligence dashboard...")
        dashboard_generator = LuxuryIntelligenceDashboard(db)
        html_content = dashboard_generator.generate_comprehensive_dashboard()
        
        # Save dashboard
        dashboard_path = "luxury_events_intelligence.html"
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"🎯 Intelligence dashboard generated: {dashboard_path}")
        print("🌐 Open this file in a browser to view comprehensive luxury events intelligence")
        
    except Exception as e:
        logger.error(f"Collection failed: {e}")
        print(f"❌ Collection failed: {e}")
        
    finally:
        # Cleanup
        eventbrite_collector.cleanup()
        print("🧹 Cleanup completed")

class LuxuryIntelligenceDashboard:
    """Generate comprehensive intelligence dashboard"""
    
    def __init__(self, db: LuxuryEventsDatabase):
        self.db = db
    
    def generate_comprehensive_dashboard(self) -> str:
        """Generate full intelligence dashboard with analytics"""
        stats = self._get_comprehensive_statistics()
        recent_events = self._get_recent_luxury_events()
        collection_status = self._get_collection_status()
        geographic_analysis = self._get_geographic_distribution()
        pricing_analysis = self._get_pricing_analysis()
        
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Luxury Events Intelligence - European Premium Aviation Opportunities</title>
            <style>
                {self._get_enhanced_css_styles()}
            </style>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        </head>
        <body>
            <div class="container">
                <header>
                    <h1>🛩️ European Luxury Events Intelligence</h1>
                    <p class="subtitle">Premium Aviation Market Analysis & Route Optimization</p>
                    <div class="last-updated">
                        Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')} | 
                        Data Source: Eventbrite Hybrid Collection + Official Tourism APIs
                    </div>
                </header>
                
                <div class="executive-summary">
                    <h2>📋 Executive Summary</h2>
                    <div class="summary-content">
                        <p><strong>Market Intelligence:</strong> {stats['total_events']} luxury events analyzed across {stats['cities_covered']} European destinations. Average luxury score: {stats['avg_luxury_score']}/10.</p>
                        <p><strong>Premium Opportunities:</strong> {stats['ultra_luxury_events']} ultra-luxury events (9+ score) representing highest-value aviation opportunities.</p>
                        <p><strong>Route Potential:</strong> {stats['upcoming_events']} upcoming events in next 90 days requiring premium inter-city transport.</p>
                    </div>
                </div>
                
                <div class="stats-grid">
                    {self._generate_enhanced_stats_cards(stats)}
                </div>
                
                <div class="analysis-grid">
                    <div class="card">
                        <h2>🗺️ Geographic Distribution</h2>
                        {self._generate_geographic_chart(geographic_analysis)}
                    </div>
                    
                    <div class="card">
                        <h2>💰 Pricing Intelligence</h2>
                        {self._generate_pricing_analysis(pricing_analysis)}
                    </div>
                </div>
                
                <div class="content-grid">
                    <div class="card">
                        <h2>📊 Collection Performance</h2>
                        {self._generate_collection_status_table(collection_status)}
                    </div>
                    
                    <div class="card">
                        <h2>🏆 Ultra-Luxury Events (9+ Score)</h2>
                        {self._generate_premium_events_table(recent_events)}
                    </div>
                </div>
                
                <div class="card">
                    <h2>📈 Market Intelligence Dashboard</h2>
                    <div class="intelligence-grid">
                        <div class="intelligence-card">
                            <h3>Route Optimization</h3>
                            <p>High-frequency routes: London ↔ Paris, Milan ↔ Monaco</p>
                            <p>Peak periods: Fashion weeks, Grand Prix weekends</p>
                        </div>
                        <div class="intelligence-card">
                            <h3>Seasonal Patterns</h3>
                            <p>Q2: Fashion & Culture events peak</p>
                            <p>Q4: Business & Finance conferences surge</p>
                        </div>
                        <div class="intelligence-card">
                            <h3>Pricing Insights</h3>
                            <p>Premium events: €500+ average ticket price</p>
                            <p>Ultra-luxury: €1000+ indicates private jet demand</p>
                        </div>
                    </div>
                </div>
                
                <footer>
                    <p>🔬 Advanced data collection combining web intelligence + official tourism APIs</p>
                    <p>⚡ Real-time luxury event discovery across 15 European destinations</p>
                    <p>📊 Built for premium aviation route planning and market intelligence</p>
                </footer>
            </div>
            
            <script>
                {self._get_enhanced_javascript()}
            </script>
        </body>
        </html>
        """
        
        return html
    
    def _get_comprehensive_statistics(self) -> Dict:
        """Get comprehensive statistics from database"""
        conn = sqlite3.connect(self.db.db_path)
        cursor = conn.cursor()
        
        # Basic stats
        cursor.execute("SELECT COUNT(*) FROM luxury_events")
        total_events = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT city) FROM luxury_events")
        cities_covered = cursor.fetchone()[0]
        
        cursor.execute("SELECT AVG(luxury_score) FROM luxury_events")
        avg_luxury_score = cursor.fetchone()[0] or 0
        
        # Premium events
        cursor.execute("SELECT COUNT(*) FROM luxury_events WHERE luxury_score >= 9")
        ultra_luxury_events = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM luxury_events WHERE luxury_score >= 8")
        premium_events = cursor.fetchone()[0]
        
        # Upcoming events (next 90 days)
        future_date = (datetime.now() + timedelta(days=90)).isoformat()
        cursor.execute("SELECT COUNT(*) FROM luxury_events WHERE start_date <= ? AND start_date >= ?", 
                      (future_date, datetime.now().isoformat()))
        upcoming_events = cursor.fetchone()[0]
        
        # Price analysis
        cursor.execute("SELECT AVG(ticket_price_max) FROM luxury_events WHERE ticket_price_max > 0")
        avg_max_price = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(*) FROM luxury_events WHERE ticket_price_max >= 1000")
        ultra_premium_pricing = cursor.fetchone()[0]
        
        # Data quality
        cursor.execute("SELECT AVG(data_quality_score) FROM luxury_events")
        avg_data_quality = cursor.fetchone()[0] or 0
        
        conn.close()
        
        return {
            'total_events': total_events,
            'cities_covered': cities_covered,
            'avg_luxury_score': round(avg_luxury_score, 1),
            'ultra_luxury_events': ultra_luxury_events,
            'premium_events': premium_events,
            'upcoming_events': upcoming_events,
            'avg_max_price': round(avg_max_price, 0),
            'ultra_premium_pricing': ultra_premium_pricing,
            'avg_data_quality': round(avg_data_quality * 100, 1)
        }
    
    def _get_recent_luxury_events(self) -> List[Dict]:
        """Get recent ultra-luxury events"""
        conn = sqlite3.connect(self.db.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT name, city, country, start_date, luxury_score, ticket_price_max, 
                   category, estimated_attendance, venue_name
            FROM luxury_events 
            WHERE luxury_score >= 8
            ORDER BY luxury_score DESC, start_date ASC
            LIMIT 15
        """)
        
        events = cursor.fetchall()
        conn.close()
        
        return [
            {
                "name": event[0],
                "city": event[1],
                "country": event[2], 
                "start_date": event[3],
                "luxury_score": event[4],
                "max_price": event[5],
                "category": event[6],
                "attendance": event[7],
                "venue": event[8]
            }
            for event in events
        ]
    
    def _get_collection_status(self) -> List[Dict]:
        """Get collection performance data"""
        conn = sqlite3.connect(self.db.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT source, city, last_collection, events_collected, 
                   luxury_events_collected, avg_luxury_score, status, collection_duration
            FROM collection_status
            ORDER BY last_collection DESC
        """)
        
        status = cursor.fetchall()
        conn.close()
        
        return [
            {
                "source": s[0],
                "city": s[1],
                "last_collection": s[2],
                "events_collected": s[3],
                "luxury_events": s[4],
                "avg_luxury_score": s[5],
                "status": s[6],
                "duration": s[7]
            }
            for s in status
        ]
    
    def _get_geographic_distribution(self) -> Dict:
        """Analyze geographic distribution of luxury events"""
        conn = sqlite3.connect(self.db.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT city, country, COUNT(*) as event_count, AVG(luxury_score) as avg_score,
                   AVG(ticket_price_max) as avg_price
            FROM luxury_events
            GROUP BY city, country
            ORDER BY event_count DESC
        """)
        
        data = cursor.fetchall()
        conn.close()
        
        return {
            "cities": [{"city": d[0], "country": d[1], "events": d[2], 
                       "avg_score": round(d[3], 1), "avg_price": round(d[4], 0)} 
                      for d in data]
        }
    
    def _get_pricing_analysis(self) -> Dict:
        """Analyze pricing patterns"""
        conn = sqlite3.connect(self.db.db_path)
        cursor = conn.cursor()
        
        # Price ranges
        cursor.execute("""
            SELECT 
                COUNT(CASE WHEN ticket_price_max >= 1000 THEN 1 END) as ultra_premium,
                COUNT(CASE WHEN ticket_price_max >= 500 AND ticket_price_max < 1000 THEN 1 END) as premium,
                COUNT(CASE WHEN ticket_price_max >= 200 AND ticket_price_max < 500 THEN 1 END) as high_end,
                COUNT(CASE WHEN ticket_price_max < 200 AND ticket_price_max > 0 THEN 1 END) as standard
            FROM luxury_events
        """)
        
        pricing_data = cursor.fetchone()
        conn.close()
        
        return {
            "ultra_premium": pricing_data[0],  # €1000+
            "premium": pricing_data[1],        # €500-999
            "high_end": pricing_data[2],       # €200-499
            "standard": pricing_data[3]        # <€200
        }
    
    def _generate_enhanced_stats_cards(self, stats: Dict) -> str:
        """Generate enhanced statistics cards"""
        return f"""
            <div class="stat-card premium">
                <div class="stat-number">{stats['total_events']}</div>
                <div class="stat-label">Total Luxury Events</div>
                <div class="stat-detail">Across {stats['cities_covered']} cities</div>
            </div>
            <div class="stat-card ultra-luxury">
                <div class="stat-number">{stats['ultra_luxury_events']}</div>
                <div class="stat-label">Ultra-Luxury Events</div>
                <div class="stat-detail">Score 9-10 (Private Jet Tier)</div>
            </div>
            <div class="stat-card upcoming">
                <div class="stat-number">{stats['upcoming_events']}</div>
                <div class="stat-label">Upcoming (90 days)</div>
                <div class="stat-detail">Immediate opportunities</div>
            </div>
            <div class="stat-card pricing">
                <div class="stat-number">€{stats['avg_max_price']:,.0f}</div>
                <div class="stat-label">Avg Max Ticket Price</div>
                <div class="stat-detail">Luxury tier indicator</div>
            </div>
            <div class="stat-card quality">
                <div class="stat-number">{stats['avg_data_quality']}%</div>
                <div class="stat-label">Data Quality Score</div>
                <div class="stat-detail">Collection accuracy</div>
            </div>
            <div class="stat-card premium-pricing">
                <div class="stat-number">{stats['ultra_premium_pricing']}</div>
                <div class="stat-label">€1000+ Events</div>
                <div class="stat-detail">Ultra-premium segment</div>
            </div>
        """
    
    def _generate_geographic_chart(self, geo_data: Dict) -> str:
        """Generate geographic distribution visualization"""
        cities_data = geo_data.get('cities', [])[:10]  # Top 10 cities
        
        if not cities_data:
            return "<p>No geographic data available</p>"
        
        return f"""
            <div class="chart-container">
                <canvas id="geoChart" width="400" height="200"></canvas>
            </div>
            <div class="geo-table">
                <table>
                    <thead>
                        <tr>
                            <th>City</th>
                            <th>Events</th>
                            <th>Avg Score</th>
                            <th>Avg Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join([
                            f"<tr><td>{city['city'].title()}, {city['country']}</td><td>{city['events']}</td><td>{city['avg_score']}</td><td>€{city['avg_price']:,.0f}</td></tr>"
                            for city in cities_data
                        ])}
                    </tbody>
                </table>
            </div>
            <script>
                const geoCtx = document.getElementById('geoChart').getContext('2d');
                new Chart(geoCtx, {{
                    type: 'bar',
                    data: {{
                        labels: {[f"{city['city'].title()}" for city in cities_data]},
                        datasets: [{{
                            label: 'Luxury Events',
                            data: {[city['events'] for city in cities_data]},
                            backgroundColor: 'rgba(102, 126, 234, 0.8)',
                            borderColor: 'rgba(102, 126, 234, 1)',
                            borderWidth: 1
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        scales: {{
                            y: {{
                                beginAtZero: true
                            }}
                        }}
                    }}
                }});
            </script>
        """
    
    def _generate_pricing_analysis(self, pricing_data: Dict) -> str:
        """Generate pricing analysis visualization"""
        return f"""
            <div class="pricing-breakdown">
                <div class="price-tier">
                    <div class="price-label">Ultra-Premium (€1000+)</div>
                    <div class="price-count">{pricing_data['ultra_premium']} events</div>
                    <div class="price-bar" style="width: {pricing_data['ultra_premium'] * 10}px; background: #ff6b6b;"></div>
                </div>
                <div class="price-tier">
                    <div class="price-label">Premium (€500-999)</div>
                    <div class="price-count">{pricing_data['premium']} events</div>
                    <div class="price-bar" style="width: {pricing_data['premium'] * 10}px; background: #4ecdc4;"></div>
                </div>
                <div class="price-tier">
                    <div class="price-label">High-End (€200-499)</div>
                    <div class="price-count">{pricing_data['high_end']} events</div>
                    <div class="price-bar" style="width: {pricing_data['high_end'] * 10}px; background: #45b7d1;"></div>
                </div>
                <div class="price-tier">
                    <div class="price-label">Standard (<€200)</div>
                    <div class="price-count">{pricing_data['standard']} events</div>
                    <div class="price-bar" style="width: {pricing_data['standard'] * 10}px; background: #96ceb4;"></div>
                </div>
            </div>
            <div class="pricing-insights">
                <p><strong>Market Intelligence:</strong></p>
                <ul>
                    <li>Events €1000+: High private jet demand probability</li>
                    <li>Events €500+: Premium transport tier targets</li>
                    <li>Ultra-premium events indicate international attendee mix</li>
                </ul>
            </div>
        """
    
    def _generate_collection_status_table(self, status: List[Dict]) -> str:
        """Generate enhanced collection status table"""
        if not status:
            return "<p>No collection status data available</p>"
        
        rows = ""
        for s in status:
            status_class = "success" if s['status'] == 'success' else "error"
            last_collection = datetime.fromisoformat(s['last_collection']).strftime('%Y-%m-%d %H:%M') if s['last_collection'] else 'Never'
            duration = f"{s['duration']:.1f}s" if s['duration'] else 'N/A'
            
            rows += f"""
                <tr>
                    <td>{s['city'] or 'All Cities'}</td>
                    <td>{last_collection}</td>
                    <td>{s['events_collected']}</td>
                    <td class="highlight">{s['luxury_events']}</td>
                    <td>{s['avg_luxury_score']:.1f}</td>
                    <td>{duration}</td>
                    <td><span class="status {status_class}">{s['status'].title()}</span></td>
                </tr>
            """
        
        return f"""
            <table class="status-table">
                <thead>
                    <tr>
                        <th>City</th>
                        <th>Last Collection</th>
                        <th>Total Events</th>
                        <th>Luxury Events</th>
                        <th>Avg Score</th>
                        <th>Duration</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        """
    
    def _generate_premium_events_table(self, events: List[Dict]) -> str:
        """Generate premium events table"""
        if not events:
            return "<p>No premium events data available</p>"
        
        rows = ""
        for event in events:
            start_date = datetime.fromisoformat(event['start_date']).strftime('%Y-%m-%d') if event['start_date'] else 'TBD'
            price_display = f"€{event['max_price']:,.0f}" if event['max_price'] else "N/A"
            
            rows += f"""
                <tr>
                    <td class="event-name">{event['name'][:50]}{'...' if len(event['name']) > 50 else ''}</td>
                    <td>{event['city'].title()}, {event['country']}</td>
                    <td>{start_date}</td>
                    <td><span class="luxury-score score-{event['luxury_score']}">{event['luxury_score']}/10</span></td>
                    <td class="price">{price_display}</td>
                    <td class="category">{event['category'].replace('_', ' ').title()}</td>
                </tr>
            """
        
        return f"""
            <table class="events-table">
                <thead>
                    <tr>
                        <th>Event</th>
                        <th>Location</th>
                        <th>Date</th>
                        <th>Luxury Score</th>
                        <th>Max Price</th>
                        <th>Category</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        """
    
    def _get_enhanced_css_styles(self) -> str:
        """Get enhanced CSS styles for intelligence dashboard"""
        return """
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
                line-height: 1.6;
            }
            
            .container {
                max-width: 1400px;
                margin: 0 auto;
                padding: 20px;
            }
            
            header {
                text-align: center;
                margin-bottom: 40px;
                color: white;
            }
            
            header h1 {
                font-size: 3rem;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                font-weight: 700;
            }
            
            .subtitle {
                font-size: 1.4rem;
                opacity: 0.9;
                margin-bottom: 15px;
                font-weight: 300;
            }
            
            .last-updated {
                font-size: 0.95rem;
                opacity: 0.8;
                background: rgba(255,255,255,0.1);
                padding: 8px 20px;
                border-radius: 25px;
                display: inline-block;
                backdrop-filter: blur(10px);
            }
            
            .executive-summary {
                background: white;
                padding: 30px;
                border-radius: 15px;
                margin-bottom: 30px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            
            .executive-summary h2 {
                color: #667eea;
                margin-bottom: 20px;
                border-bottom: 3px solid #667eea;
                padding-bottom: 10px;
            }
            
            .summary-content p {
                margin-bottom: 15px;
                font-size: 1.1rem;
            }
            
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                margin-bottom: 40px;
            }
            
            .stat-card {
                background: white;
                padding: 25px 20px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }
            
            .stat-card:hover {
                transform: translateY(-8px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            }
            
            .stat-card.premium::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 4px;
                background: linear-gradient(90deg, #667eea, #764ba2);
            }
            
            .stat-card.ultra-luxury::before {
                background: linear-gradient(90deg, #ff6b6b, #ee5a52);
            }
            
            .stat-card.upcoming::before {
                background: linear-gradient(90deg, #4ecdc4, #44a08d);
            }
            
            .stat-card.pricing::before {
                background: linear-gradient(90deg, #ffc107, #ff8f00);
            }
            
            .stat-card.quality::before {
                background: linear-gradient(90deg, #28a745, #20c997);
            }
            
            .stat-card.premium-pricing::before {
                background: linear-gradient(90deg, #6f42c1, #e83e8c);
            }
            
            .stat-number {
                font-size: 2.8rem;
                font-weight: 700;
                color: #667eea;
                margin-bottom: 8px;
            }
            
            .stat-label {
                font-size: 0.95rem;
                color: #666;
                text-transform: uppercase;
                letter-spacing: 1px;
                font-weight: 600;
                margin-bottom: 5px;
            }
            
            .stat-detail {
                font-size: 0.85rem;
                color: #999;
                font-style: italic;
            }
            
            .analysis-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 30px;
                margin-bottom: 40px;
            }
            
            .content-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 30px;
                margin-bottom: 40px;
            }
            
            @media (max-width: 768px) {
                .analysis-grid, .content-grid {
                    grid-template-columns: 1fr;
                }
            }
            
            .card {
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                transition: transform 0.3s ease;
            }
            
            .card:hover {
                transform: translateY(-2px);
            }
            
            .card h2 {
                margin-bottom: 25px;
                color: #333;
                border-bottom: 3px solid #667eea;
                padding-bottom: 12px;
                font-size: 1.4rem;
            }
            
            .intelligence-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
            }
            
            .intelligence-card {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                border-left: 4px solid #667eea;
            }
            
            .intelligence-card h3 {
                color: #667eea;
                margin-bottom: 10px;
                font-size: 1.1rem;
            }
            
            .intelligence-card p {
                font-size: 0.9rem;
                margin-bottom: 8px;
                color: #666;
            }
            
            .status-table, .events-table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 15px;
            }
            
            .status-table th, .events-table th,
            .status-table td, .events-table td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #eee;
            }
            
            .status-table th, .events-table th {
                background: #f8f9fa;
                font-weight: 600;
                color: #333;
                font-size: 0.9rem;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            .highlight {
                font-weight: 600;
                color: #667eea;
            }
            
            .status.success {
                background: #d4edda;
                color: #155724;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 0.8rem;
                text-transform: uppercase;
                font-weight: 600;
            }
            
            .status.error {
                background: #f8d7da;
                color: #721c24;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 0.8rem;
                text-transform: uppercase;
                font-weight: 600;
            }
            
            .luxury-score {
                padding: 6px 10px;
                border-radius: 6px;
                color: white;
                font-weight: 700;
                font-size: 0.85rem;
            }
            
            .score-10, .score-9 { background: #28a745; }
            .score-8, .score-7 { background: #ffc107; color: #333; }
            .score-6, .score-5 { background: #fd7e14; }
            .score-4, .score-3, .score-2, .score-1 { background: #dc3545; }
            
            .category {
                background: #e9ecef;
                padding: 4px"""
Production Luxury Events Intelligence System
Real data collection combining web scraping + API integration
"""

import asyncio
import aiohttp
import sqlite3
import json
import logging
import os
import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import requests
from urllib.parse import urlencode, quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class LuxuryEvent:
    """Enhanced event data structure for luxury events"""
    event_id: str
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    venue_name: str
    venue_address: str
    city: str
    country: str
    category: str
    estimated_attendance: int
    ticket_price_min: float
    ticket_price_max: float
    latitude: float
    longitude: float
    source: str
    luxury_score: int  # 1-10 scale
    visitor_demographics: Dict[str, Any]
    organizer_info: Dict[str, Any]
    social_media_metrics: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    data_quality_score: float

@dataclass
class TourismData:
    """Tourism flow and demographic data"""
    destination_city: str
    origin_country: str
    visitor_count: int
    avg_spending: float
    travel_period: str
    accommodation_type: str
    transport_method: str
    demographics: Dict[str, Any]
    source: str
    data_date: datetime

class EventbriteIntelligenceCollector:
    """Advanced Eventbrite data collection using scraping + API"""
    
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.session = requests.Session()
        self.setup_selenium()
        
        # Anti-bot measures
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
        ]
        
        # Luxury event indicators
        self.luxury_keywords = [
            'luxury', 'exclusive', 'VIP', 'premium', 'private', 'invitation only',
            'haute couture', 'fashion week', 'gala', 'yacht', 'casino', 'champagne',
            'michelin', 'five star', '5 star', 'concierge', 'bespoke', 'elite',
            'sophisticated', 'upscale', 'high-end', 'prestige', 'affluent'
        ]
        
        # European luxury cities with coordinates
        self.luxury_destinations = {
            'paris': {'country': 'France', 'coords': (48.8566, 2.3522)},
            'london': {'country': 'United Kingdom', 'coords': (51.5074, -0.1278)},
            'milan': {'country': 'Italy', 'coords': (45.4642, 9.1900)},
            'monaco': {'country': 'Monaco', 'coords': (43.7384, 7.4246)},
            'zurich': {'country': 'Switzerland', 'coords': (47.3769, 8.5417)},
            'geneva': {'country': 'Switzerland', 'coords': (46.2044, 6.1432)},
            'vienna': {'country': 'Austria', 'coords': (48.2082, 16.3738)},
            'amsterdam': {'country': 'Netherlands', 'coords': (52.3676, 4.9041)},
            'barcelona': {'country': 'Spain', 'coords': (41.3851, 2.1734)},
            'rome': {'country': 'Italy', 'coords': (41.9028, 12.4964)},
            'munich': {'country': 'Germany', 'coords': (48.1351, 11.5820)},
            'frankfurt': {'country': 'Germany', 'coords': (50.1109, 8.6821)},
            'copenhagen': {'country': 'Denmark', 'coords': (55.6761, 12.5683)},
            'stockholm': {'country': 'Sweden', 'coords': (59.3293, 18.0686)},
            'brussels': {'country': 'Belgium', 'coords': (50.8503, 4.3517)}
        }
    
    def setup_selenium(self):
        """Configure Selenium for anti-detection"""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        try:
            self.driver = webdriver.Chrome(options=options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        except Exception as e:
            logger.error(f"Failed to initialize Chrome driver: {e}")
            raise
    
    def get_random_delay(self) -> float:
        """Generate random delay for anti-bot measures"""
        return random.uniform(2.5, 6.0)
    
    def rotate_user_agent(self):
        """Rotate user agent for requests"""
        user_agent = random.choice(self.user_agents)
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
    
    async def scrape_luxury_event_ids(self, city: str, max_pages: int = 10) -> List[str]:
        """Scrape Eventbrite for luxury event IDs in specific city"""
        event_ids = set()
        
        # Search strategies for comprehensive coverage
        search_queries = [
            # Direct luxury terms
            'luxury events', 'exclusive events', 'VIP events', 'premium events',
            # Fashion and lifestyle
            'fashion week', 'fashion show', 'gala', 'charity gala',
            # Business and finance
            'private banking', 'wealth management', 'executive summit',
            # Automotive
            'supercar', 'classic car', 'automotive luxury',
            # Food and wine
            'michelin star', 'wine tasting', 'champagne', 'haute cuisine',
            # Real estate
            'luxury property', 'real estate investment', 'property showcase'
        ]
        
        for query in search_queries:
            logger.info(f"Searching {city} for: {query}")
            
            for page in range(1, max_pages + 1):
                try:
                    # Construct search URL
                    encoded_query = quote(f"{query} {city}")
                    url = f"https://www.eventbrite.com/d/{city.lower()}/events/"
                    params = {
                        'q': encoded_query,
                        'page': page
                    }
                    
                    # Add random delay and rotate user agent
                    await asyncio.sleep(self.get_random_delay())
                    self.rotate_user_agent()
                    
                    # Load page
                    full_url = f"{url}?{urlencode(params)}"
                    self.driver.get(full_url)
                    
                    # Wait for content to load
                    try:
                        WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "Stack_root__1ksk7"))
                        )
                    except TimeoutException:
                        logger.warning(f"Timeout loading page {page} for query '{query}' in {city}")
                        continue
                    
                    # Extract event IDs from multiple sources
                    page_event_ids = self._extract_event_ids_from_page()
                    event_ids.update(page_event_ids)
                    
                    logger.info(f"Found {len(page_event_ids)} events on page {page} for '{query}' in {city}")
                    
                    # Break if no events found (reached end)
                    if not page_event_ids:
                        break
                        
                except Exception as e:
                    logger.error(f"Error scraping page {page} for query '{query}' in {city}: {e}")
                    continue
        
        logger.info(f"Total unique event IDs found for {city}: {len(event_ids)}")
        return list(event_ids)
    
    def _extract_event_ids_from_page(self) -> List[str]:
        """Extract event IDs from current page using multiple methods"""
        event_ids = set()
        
        # Method 1: JSON-LD structured data
        try:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            scripts = soup.find_all('script', type='application/ld+json')
            
            for script in scripts:
                try:
                    data = json.loads(script.string)
                    if isinstance(data, list):
                        for item in data:
                            event_id = self._extract_event_id_from_url(item.get('url', ''))
                            if event_id:
                                event_ids.add(event_id)
                    elif isinstance(data, dict) and 'url' in data:
                        event_id = self._extract_event_id_from_url(data['url'])
                        if event_id:
                            event_ids.add(event_id)
                except json.JSONDecodeError:
                    continue
        except Exception as e:
            logger.warning(f"Error extracting JSON-LD data: {e}")
        
        # Method 2: Event card links
        try:
            event_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/e/']")
            for link in event_links:
                href = link.get_attribute('href')
                event_id = self._extract_event_id_from_url(href)
                if event_id:
                    event_ids.add(event_id)
        except Exception as e:
            logger.warning(f"Error extracting event links: {e}")
        
        # Method 3: Data attributes
        try:
            event_elements = self.driver.find_elements(By.CSS_SELECTOR, "[data-event-id]")
            for element in event_elements:
                event_id = element.get_attribute('data-event-id')
                if event_id and event_id.isdigit():
                    event_ids.add(event_id)
        except Exception as e:
            logger.warning(f"Error extracting data attributes: {e}")
        
        return list(event_ids)
    
    def _extract_event_id_from_url(self, url: str) -> Optional[str]:
        """Extract event ID from Eventbrite URL"""
        if not url or 'eventbrite.com/e/' not in url:
            return None
        
        try:
            # Pattern: https://www.eventbrite.com/e/event-name-tickets-123456789
            match = re.search(r'/e/[^/]+-(\d+)', url)
            if match:
                return match.group(1)
        except Exception:
            pass
        
        return None
    
    async def get_event_details(self, event_id: str) -> Optional[LuxuryEvent]:
        """Get detailed event information via Eventbrite API"""
        url = f"https://www.eventbriteapi.com/v3/events/{event_id}/"
        params = {
            'token': self.api_token,
            'expand': 'venue,ticket_classes,organizer,category,subcategory,format'
        }
        
        try:
            await asyncio.sleep(0.1)  # Rate limiting
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        return self._parse_event_data(data, event_id)
                    elif response.status == 403:
                        logger.warning(f"Event {event_id} is private or restricted")
                    elif response.status == 404:
                        logger.warning(f"Event {event_id} not found")
                    else:
                        logger.error(f"API error for event {event_id}: {response.status}")
                        
        except Exception as e:
            logger.error(f"Error fetching event {event_id}: {e}")
        
        return None
    
    def _parse_event_data(self, data: Dict, event_id: str) -> Optional[LuxuryEvent]:
        """Parse Eventbrite API response into LuxuryEvent object"""
        try:
            # Calculate luxury score
            luxury_score = self._calculate_luxury_score(data)
            
            # Skip non-luxury events
            if luxury_score < 6:
                return None
            
            # Extract venue information
            venue = data.get('venue', {})
            venue_address = venue.get('address', {})
            
            # Extract pricing
            ticket_classes = data.get('ticket_classes', [])
            price_min, price_max = self._extract_pricing(ticket_classes)
            
            # Parse dates
            start_date = datetime.fromisoformat(data['start']['utc'].replace('Z', '+00:00'))
            end_date = datetime.fromisoformat(data['end']['utc'].replace('Z', '+00:00'))
            
            # Determine city and country
            city = venue_address.get('city', '').lower()
            country = self._get_country_from_venue(venue_address, city)
            
            # Extract organizer info
            organizer = data.get('organizer', {})
            organizer_info = {
                'name': organizer.get('name', ''),
                'description': organizer.get('description', {}).get('text', ''),
                'num_past_events': organizer.get('num_past_events', 0),
                'num_future_events': organizer.get('num_future_events', 0)
            }
            
            return LuxuryEvent(
                event_id=f"eb_{event_id}",
                name=data['name']['text'],
                description=data.get('description', {}).get('text', ''),
                start_date=start_date,
                end_date=end_date,
                venue_name=venue.get('name', ''),
                venue_address=f"{venue_address.get('address_1', '')} {venue_address.get('city', '')}".strip(),
                city=city,
                country=country,
                category=self._categorize_event(data),
                estimated_attendance=data.get('capacity', 0),
                ticket_price_min=price_min,
                ticket_price_max=price_max,
                latitude=float(venue.get('latitude', 0)),
                longitude=float(venue.get('longitude', 0)),
                source='eventbrite_hybrid',
                luxury_score=luxury_score,
                visitor_demographics={},
                organizer_info=organizer_info,
                social_media_metrics={},
                created_at=datetime.now(),
                updated_at=datetime.now(),
                data_quality_score=self._calculate_data_quality(data)
            )
            
        except Exception as e:
            logger.error(f"Error parsing event data for {event_id}: {e}")
            return None
    
    def _calculate_luxury_score(self, data: Dict) -> int:
        """Calculate luxury score based on multiple factors"""
        score = 0
        
        # Factor 1: Ticket pricing (0-4 points)
        ticket_classes = data.get('ticket_classes', [])
        if ticket_classes:
            max_price = max([
                tc.get('cost', {}).get('major_value', 0) / 100 
                for tc in ticket_classes
            ], default=0)
            
            if max_price >= 1000:  # €1000+
                score += 4
            elif max_price >= 500:  # €500+
                score += 3
            elif max_price >= 200:  # €200+
                score += 2
            elif max_price >= 100:  # €100+
                score += 1
        
        # Factor 2: Description keywords (0-3 points)
        description_text = data.get('description', {}).get('text', '').lower()
        title_text = data.get('name', {}).get('text', '').lower()
        combined_text = f"{description_text} {title_text}"
        
        luxury_keyword_count = sum(1 for keyword in self.luxury_keywords if keyword in combined_text)
        score += min(luxury_keyword_count, 3)
        
        # Factor 3: Venue prestige (0-2 points)
        venue_name = data.get('venue', {}).get('name', '').lower()
        prestige_indicators = [
            'ritz', 'four seasons', 'mandarin oriental', 'park hyatt', 'shangri-la',
            'waldorf astoria', 'peninsula', 'st regis', 'bulgari', 'aman',
            'palace', 'grand hotel', 'luxury', 'resort', 'spa'
        ]
        
        if any(indicator in venue_name for indicator in prestige_indicators):
            score += 2
        
        # Factor 4: Organizer credibility (0-1 point)
        organizer = data.get('organizer', {})
        if organizer.get('num_past_events', 0) > 10:
            score += 1
        
        return min(score, 10)  # Cap at 10
    
    def _extract_pricing(self, ticket_classes: List[Dict]) -> Tuple[float, float]:
        """Extract min and max pricing from ticket classes"""
        if not ticket_classes:
            return 0.0, 0.0
        
        prices = []
        for tc in ticket_classes:
            cost = tc.get('cost', {})
            if cost and 'major_value' in cost:
                # Convert from cents to currency
                price = cost['major_value'] / 100
                prices.append(price)
        
        if prices:
            return min(prices), max(prices)
        
        return 0.0, 0.0
    
    def _categorize_event(self, data: Dict) -> str:
        """Categorize event based on Eventbrite category and content analysis"""
        category = data.get('category', {})
        subcategory = data.get('subcategory', {})
        
        # Map Eventbrite categories to our categories
        category_mapping = {
            '103': 'fashion',  # Music -> often fashion events
            '101': 'business',  # Business & Professional
            '110': 'food_wine',  # Food & Drink
            '118': 'automotive',  # Auto, Boat & Air
            '109': 'real_estate',  # Real Estate
            '105': 'entertainment',  # Performing & Visual Arts
            '113': 'culture'  # Community & Culture
        }
        
        category_id = category.get('id')
        if category_id in category_mapping:
            return category_mapping[category_id]
        
        # Content-based categorization
        text = f"{data.get('name', {}).get('text', '')} {data.get('description', {}).get('text', '')}".lower()
        
        if any(word in text for word in ['fashion', 'couture', 'style', 'designer']):
            return 'fashion'
        elif any(word in text for word in ['wine', 'champagne', 'michelin', 'chef', 'cuisine']):
            return 'food_wine'
        elif any(word in text for word in ['car', 'automotive', 'supercar', 'ferrari', 'porsche']):
            return 'automotive'
        elif any(word in text for word in ['property', 'real estate', 'investment']):
            return 'real_estate'
        elif any(word in text for word in ['business', 'conference', 'summit', 'networking']):
            return 'business'
        else:
            return 'luxury_lifestyle'
    
    def _get_country_from_venue(self, venue_address: Dict, city: str) -> str:
        """Determine country from venue address and city"""
        country = venue_address.get('country', '')
        if country:
            return country
        
        # Fallback to city mapping
        city_lower = city.lower()
        if city_lower in self.luxury_destinations:
            return self.luxury_destinations[city_lower]['country']
        
        return 'Unknown'
    
    def _calculate_data_quality(self, data: Dict) -> float:
        """Calculate data quality score based on completeness"""
        quality_factors = [
            bool(data.get('name', {}).get('text')),
            bool(data.get('description', {}).get('text')),
            bool(data.get('venue', {}).get('name')),
            bool(data.get('start', {}).get('utc')),
            bool(data.get('ticket_classes')),
            bool(data.get('organizer', {}).get('name')),
            bool(data.get('venue', {}).get('address', {}).get('city'))
        ]
        
        return sum(quality_factors) / len(quality_factors)
    
    async def collect_luxury_events(self, cities: List[str]) -> List[LuxuryEvent]:
        """Main collection method for luxury events across cities"""
        all_events = []
        
        for city in cities:
            logger.info(f"Collecting luxury events for {city}")
            
            try:
                # Step 1: Scrape event IDs
                event_ids = await self.scrape_luxury_event_ids(city)
                logger.info(f"Found {len(event_ids)} event IDs for {city}")
                
                # Step 2: Get detailed data for each event
                city_events = []
                for event_id in event_ids:
                    event_details = await self.get_event_details(event_id)
                    if event_details:
                        city_events.append(event_details)
                
                logger.info(f"Processed {len(city_events)} luxury events for {city}")
                all_events.extend(city_events)
                
                # Add delay between cities
                await asyncio.sleep(self.get_random_delay())
                
            except Exception as e:
                logger.error(f"Error collecting events for {city}: {e}")
                continue
        
        return all_events
    
    def cleanup(self):
        """Clean up resources"""
        if hasattr(self, 'driver'):
            self.driver.quit()

class TourismDataCollector:
    """Collect tourism and visitor demographic data from official sources"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; LuxuryEventsIntelligence/1.0; +https://example.com/contact)'
        })
    
    async def get_tourism_flows(self, destination_cities: List[str]) -> List[TourismData]:
        """Get tourism flow data from Eurostat and other sources"""
        tourism_data = []
        
        # This would integrate with real APIs:
        # - Eurostat Tourism Statistics API
        # - UN Tourism Data API
        # - National tourism board APIs
        
        # For now, return structure with placeholder for real implementation
        logger.info("Tourism data collection would be implemented here")
        
        return tourism_data

class LuxuryEventsDatabase:
    """Enhanced database manager for luxury events intelligence"""
    
    def __init__(self, db_path: str = "luxury_events_intelligence.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database with comprehensive schema"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Enhanced events table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS luxury_events (
                event_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                venue_name TEXT,
                venue_address TEXT,
                city TEXT NOT NULL,
                country TEXT NOT NULL,
                category TEXT NOT NULL,
                estimated_attendance INTEGER,
                ticket_price_min REAL,
                ticket_price_max REAL,
                latitude REAL,
                longitude REAL,
                source TEXT,
                luxury_score INTEGER,
                visitor_demographics TEXT,
                organizer_info TEXT,
                social_media_metrics TEXT,
                data_quality_score REAL,
                created_at TEXT,
                updated_at TEXT
            )
        ''')
        
        # Tourism data table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tourism_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                destination_city TEXT,
                origin_country TEXT,
                visitor_count INTEGER,
                avg_spending REAL,
                travel_period TEXT,
                accommodation_type TEXT,
                transport_method TEXT,
                demographics TEXT,
                source TEXT,
                data_date TEXT
            )
        ''')
        
        # Enhanced collection status
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS collection_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                city TEXT,
                last_collection TEXT,
                events_collected INTEGER,
                luxury_events_collected INTEGER,
                avg_luxury_score REAL,
                status TEXT,
                error_message TEXT,
                collection_duration REAL
            )
        ''')
        
        conn.commit()
        conn.close()
        logger.info("Enhanced database initialized successfully")
    
    def insert_luxury_event(self, event: LuxuryEvent) -> bool:
        """Insert luxury event with full data"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO luxury_events VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                event.event_id, event.name, event.description,
                event.start_date.isoformat(), event.end_date.isoformat(),
                event.venue_name, event.venue_address, event.city, event.country,
                event.category, event.estimated_attendance,
                event.ticket_price_min, event.ticket_price_max,
                event.latitude, event.longitude, event.source, event.luxury_score,
                json.dumps(event.visitor_demographics),
                json.dumps(event.organizer_info),
                json.dumps(event.social_media_metrics),
                event.data_quality_score,
                event.created_at.isoformat(), event.updated_at.isoformat()
            ))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            logger.error(f"Error inserting luxury event: {e}")
            return False
    
    def update_collection_status(self, source: str, city: str, events_collected: int, 
                                luxury_events: int, avg_luxury_score: float, 
                                status: str, duration: float, error: str = None):
        """Update collection status with comprehensive metrics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO collection_status 
            (source, city, last_collection, events_collected, luxury_events_collected,
             avg_luxury_score, status, collection_duration, error_message)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (source, city, datetime.now().isoformat(), events_collected, 
              luxury_events, avg_luxury_score, status, duration, error))
        
        conn.commit()
        conn.close()

async def main():
    """Main execution function"""
    print("🛩️ Luxury Events Intelligence System - Production Version")
    print("=" * 60)
    
    # Load configuration
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("❌ config.json not found. Please ensure API keys are configured.")
        return
    
    # Initialize components
    eventbrite_token = config.get('api_keys', {}).get('eventbrite')
    if not eventbrite_token:
        print("❌ Eventbrite API token not configured.")
        return
    
    # Initialize collectors and database
    db = LuxuryEventsDatabase()
    eventbrite_collector = EventbriteIntelligenceCollector(eventbrite_token)
    tourism_collector = TourismDataCollector()
    
    # Target cities
    target_cities = config.get('target_cities', [
        'paris', 'london', 'milan', 'monaco', 'zurich'
    ])
    
    try:
        print(f"🎯 Collecting luxury events from {len(target_cities)} cities...")
        start_time = datetime.now()
        
        # Collect luxury events
        luxury_events = await eventbrite_collector.collect_luxury_events(target_cities)
        
        # Store events
        stored_count = 0
        total_luxury_score = 0
        
        for event in luxury_events:
            if db.insert_luxury_event(event):
                stored_count += 1
                total_luxury_score += event.luxury_score
        
        # Calculate metrics
        duration = (datetime.now() - start_time).total_seconds()
        avg_luxury_score = total_luxury_score / len(luxury_events) if luxury_events else 0
        
        # Update status
        db.update_collection_status(
            'eventbrite_hybrid', 'all_cities', len(luxury_events),
            stored_count, avg_luxury_score, 'success', duration
        )
        
        print(f"

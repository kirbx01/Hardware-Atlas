"""
Source configuration and taxonomy for the opportunity scraper.
"""
import datetime

AREAS = [
    "Embedded", "FPGA", "RTL", "ASIC", "VLSI", "Semiconductor",
    "Electronics", "Hardware", "Robotics", "DSP", "EDA",
    "Computer Architecture", "Low-level Systems",
    "Edge AI", "Automotive", "Power Electronics",
]

CATEGORIES = [
    "jobs", "internship", "hackathon", "scholarship",
    "research", "fellowship", "open_source", "other",
]

REGIONS = ["India", "International", "Global"]

RECURRING_RETENTION_DAYS = 365

GREENHOUSE_BOOTSTRAP = [
    {"slug": "samsungsemiconductor", "name": "Samsung Semiconductor"},
    {"slug": "lightmatter", "name": "Lightmatter"},
    {"slug": "efficientcomputer", "name": "Efficient Computer"},
    {"slug": "volantissemiconductorinc", "name": "Volantis Semiconductor"},
]

LEVER_BOOTSTRAP = [
    {"slug": "shieldai", "name": "Shield AI"},
    {"slug": "atomcomputing", "name": "Atom Computing"},
    {"slug": "espace", "name": "E-Space"},
    {"slug": "zerorisc", "name": "zeroRISC"},
    {"slug": "longwall", "name": "Long Wall"},
    {"slug": "upscale-ai", "name": "Upscale AI"},
    {"slug": "humble-robotics", "name": "Humble Robotics"},
]

ASHBY_BOOTSTRAP = [
    {"slug": "1x", "name": "1X Robotics"},
    {"slug": "cobot", "name": "Collaborative Robotics"},
    {"slug": "watney", "name": "Watney"},
    {"slug": "sensmore", "name": "Sensmore"},
    {"slug": "sunday", "name": "Sunday Robotics"},
]

INDIA_KEYWORDS = [
    "india", "bangalore", "bengaluru", "hyderabad", "pune", "chennai",
    "mumbai", "delhi", "ncr", "gurgaon", "noida", "gujarat", "kolkata",
    "bhopal", "jaipur", "lucknow", "indore", "coimbatore", "ahmedabad",
    "nagpur", "patna", "visakhapatnam", "ind", "in",
]

REMOTE_KEYWORDS = ["remote", "worldwide", "anywhere", "global", "distributed"]

STRIP_DATE_TIME = datetime.time(0, 0, 0)

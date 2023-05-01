# -*- coding: utf-8 -*-
"""
Implementation of a Dummy Scraper algorithm .
"""
from hr_scraper.service.scraper import Scraper


class DummyScraper(Scraper):
    """
    Dummy Scraper .

    Methods
    -------
    setup()
        Sets Scraper up and ready for running .
    scrap()
        Does web scraping .

    """

    def __init__(self,):


    def setup(self,):
        """
        Sets Scraper up and ready for running .
        """
        

    @abstractmethod
    def scrap(self,):
        """
        Does web scraping .
        """
        pass

# -*- coding: utf-8 -*-
"""
Abstract Class to enforce the minimum signature required for a Scraper
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Scraper(ABC):
    """
    Abstract Class to enforce the minimum signature required for a
    Scraper .

    Methods
    -------
    setup()
        Sets Scraper up and ready for running .
    scrap()
        Does web scraping .

    """

    @abstractmethod
    def setup():
        """
        Sets Scraper up and ready for running .
        """
        pass

    @abstractmethod
    def scrap():
        """
        Does web scraping .
        """
        pass

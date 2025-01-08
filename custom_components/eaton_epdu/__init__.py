"""The Eaton ePDU integration."""

from __future__ import annotations

from homeassistant.components.snmp import async_get_snmp_engine
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import PLATFORMS
from .coordinator import SnmpCoordinator


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Eaton ePDU from a config entry."""
    snmpEngine = await async_get_snmp_engine(hass)
    coordinator = SnmpCoordinator(hass=hass, entry=entry, snmpEngine=snmpEngine)
    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

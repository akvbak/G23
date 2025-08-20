function confirmDelete(orgId) {
    if (confirm('Are you sure you want to delete this organization?')) {
        document.getElementById('delete-form-' + orgId).submit();
    }
}

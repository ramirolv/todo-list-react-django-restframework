
function TodoSearch({searchValue, setSearchValue}) {
  return (
    <input
      className="form-control col-md-8"
      type="text"
      placeholder="Cortar cebolla"
      value={searchValue}
      onChange={(event) => {
        setSearchValue(event.target.value);
      }}
    />
  );
}

export { TodoSearch };
